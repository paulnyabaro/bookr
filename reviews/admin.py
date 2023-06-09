from django.contrib import admin
from .models import Publisher, Book, Contributor, Review, BookContributor


admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Contributor)
admin.site.register(Publisher)
admin.site.register(Review)