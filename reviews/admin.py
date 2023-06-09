from django.contrib import admin
from .models import Book, BookContributor, Contributor, Publisher, Review


admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Contributor)
admin.site.register(Publisher)
admin.site.register(Review)