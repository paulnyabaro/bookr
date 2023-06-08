from django.shortcuts import render, get_object_or_404

from .models import Book, Review
from .utils import average_rating


def index(request):
    name = 'Josephine'
    books = Book.objects.count()
    return render(request, 'index.html', {'name': name, 'books': books})

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)

        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book':book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
            
    context = {
        'book_list': book_list
    }
    return render(request, 'books_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.review_set.all()
    context = {'book': book, 'reviews': reviews}
    return render(request, 'book_detail.html', context)
    