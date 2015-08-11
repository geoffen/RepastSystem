from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class BookManager(models.Manager):
    def get_book_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


#  django1.8 change get_query_set to get_queryset..  so ...
class BookQuerySet(models.Manager):
    def get_queryset(self):
        return super(BookQuerySet, self).get_queryset().filter(title__icontains='Python')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    objects = models.Manager()

    bookObj = BookManager()
    bookQS = BookQuerySet()

    def __unicode__(self):
        return self.title
