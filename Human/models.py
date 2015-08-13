#  django1.8 remove localflavor from django.contrib,
#  first we should install localflavor then add to settings.py->installed_app

from localflavor.us.models import USStateField
from django.db import models
from ckeditor.fields import RichTextField


class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(sex__icontains='M')


class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(sex__icontains='F')


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    state = USStateField()  # Yes, this is U.S.-centric...

    content = RichTextField('??')

    objects = models.Manager()

    men = MaleManager()
    women = FemaleManager()

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if datetime.date(1945, 8, 1) <= self.birth_date <= datetime.date(1964, 12, 31):
            return "Baby boomer"
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        return "Post-boomer"

    def is_midwestern(self):
        "Returns True if this person is from the Midwest."
        return self.state in ('IL', 'WI', 'MI', 'IN', 'OH', 'IA', 'MO')

    def _get_full_name(self):
        "Returns the person's full name."
        return u'%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)
