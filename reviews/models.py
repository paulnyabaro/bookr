from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='The name of the Publisher.')
    website = models.URLField(help_text='The Publisher\'s website')
    email = models.EmailField(help_text='The Publisher\'s email address')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text='The title of the book')
    publication_date = models.DateField(verbose_name='Date the book was published')
    isbn = models.CharField(max_length=20, verbose_name='ISBN number of the book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text='The contributor\'s first name or names')
    last_name = models.CharField(max_length=50, help_text='The contributor\'s last name or names')
    email = models.EmailField(help_text='The contact email for the contributor')

    def __str__(self):
        return self.first_name