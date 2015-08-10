from __future__ import unicode_literals

from django.db import models
from datetime import date
# from django.utils import timezone

# Create your models here.


# class Country(models.Model):
#     countryName = models.CharField(max_length=30, default='none')
#
#     def __unicode__(self):
#         return self.countryName


class UserInformation(models.Model):
    username = models.CharField(max_length=16, default='test')
    password = models.CharField(max_length=16, default='test')
    createTime = models.DateField(default=date.today())
    # createTime = models.DateTimeField('Create Time : ', default=timezone.now)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    # country = models.ForeignKey(Country)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']
