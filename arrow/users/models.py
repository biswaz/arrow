from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    branches = (
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('IT', 'IT'),
    ('ME', 'ME'),
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    #students
    admn_no = models.IntegerField(blank=False)
    semester = models.IntegerField()
    branch = models.CharField(max_length=2, choices=branches)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
