from django.shortcuts import render


def index(request):
    name = 'Josephine'
    return render(request, 'index.html', {'name': name})
