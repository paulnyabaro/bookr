from django.shortcuts import render


def index(request):
    name = 'Josephine'
    return render(request, '_base.html', {'name': name})
