from django.shortcuts import render
from .models import NorthFork

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def map_page(request):
    data = NorthFork.objects.using('creek_data').all()[1:100]

    for row in data:
        print(row)
    return render(request, 'map.html')


