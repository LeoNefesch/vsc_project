from array import array

from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', 'some string'],
        'obj': {
            'car': 'BMW',
            'age': 25,
            'hobby': 'guitar'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
