# from django.contrib import admin
from django.contrib.admin import AdminSite
from reviews.models import Book, BookContributor, Contributor, Publisher, Review

class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'
    
admin_site = BookrAdminSite(name='bookr')


admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Contributor)
admin_site.register(Publisher)
admin_site.register(Review)