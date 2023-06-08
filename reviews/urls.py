from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='books_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]