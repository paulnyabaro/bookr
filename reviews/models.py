from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='The name of the Publisher.')
    website = models.URLField(help_text='The Publisher\'s website')
    email = models.EmailField(help_text='The Publisher\'s email address')


class Book(models.Model):
    title = models.CharField(max_length=200, help_text='The title of the book')
    publication_date = models.DateField(verbose_name='Date the book was published')
    isbn = models.CharField(max_length=20, verbose_name='ISBN number of the book')