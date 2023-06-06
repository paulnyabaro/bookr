from django.shortcuts import render
from .models import Book


def index(request):
    name = 'Josephine'
    books = Book.objects.count()
    return render(request, 'index.html', {'name': name, 'books': books})
