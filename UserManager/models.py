from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# from datetime import datetime
# Create your models here.


class Country(models.Model):
    countryName = models.CharField(max_length=30, default='none')
    capital = models.CharField(max_length=30, default='none')
    population = models.IntegerField(default=12)
    countryCode = models.CharField(max_length=5, default='+86')

    def __unicode__(self):
        return self.countryName

    class Meta:
        ordering = ['countryName']


class UserInformation(models.Model):
    username = models.CharField(max_length=16, default='test')
    password = models.CharField(max_length=16, default='test')
    createTime = models.DateField(blank=True, null=True, default=timezone.now)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']
