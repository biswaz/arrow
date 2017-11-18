from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _



class User(AbstractUser):
    branches = (
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('IT', 'IT'),
    ('ME', 'ME'),
    )
    designations = (
    ('st', 'STUDENT'),
    ('tu', 'TUTOR'),
    ('ho', 'HOD'),
    ('of', 'OFFICE STAFF'),
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    designation = models.CharField(max_length=2, choices=designations)

    #students
    admn_no = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    branch = models.CharField(max_length=3, choices=branches, blank=True)
    parent_name = models.CharField(_('Name of parent'), blank=True, max_length=255)

    #staff

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
