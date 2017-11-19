from django.db import models
from arrow.users.models import User

# Create your models here.
class Application(models.Model):
    types = (
    ('SSLC', 'SSLC'),
    ('+2', '+2'),
    ('EMB', 'Embassy Attestation'),
    ('BNK1', 'Bank Loan - 1 Year'),
    ('BNK4', 'Bank Loan - 4 Years'),
    ('CHAR', 'Character Certificate'),
    ('NRSD', 'Non Receipt of Stipend'),
    ('NRLP', 'Non Receipt of Laptop'),
    ('NRSP', 'Non Receipt of Scholarship'),
    ('OTH', 'Other'),
    )

    applicant = models.ForeignKey('users.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=types)
    other = models.CharField(max_length=100, blank=True)#Description of other field
    hierarchy_level = models.IntegerField(default=0)

    def __str__(self):
        return self.applicant.name + "'s " + self.get_type_display() + " application"


#Defines the path --HA01
class Hierarchy(models.Model):
    class Meta:
        verbose_name_plural = 'hierarchies'

    name = models.CharField(max_length=5)#HA01
    sl_no = models.IntegerField()
    designation = models.CharField(max_length=2, choices=User.designations)

    def __str__(self):
        return self.name


#Defines the hierarchy of a set of applications
class ApplicationType(models.Model):
    name = models.CharField(max_length=4, choices=Application.types, unique=True)#SSLC
    hierarchy = models.ForeignKey('Hierarchy', on_delete=models.CASCADE)#HA01


class Status(models.Model):
    class Meta:
        verbose_name_plural = 'statuses'

    application = models.ForeignKey('application', on_delete=models.CASCADE)
    sl_no = models.IntegerField()
    date_created = models.DateTimeField()
    remarks = models.CharField(max_length=100, blank=True)
    #TODO: acquire the current words used to describe a forwarding
