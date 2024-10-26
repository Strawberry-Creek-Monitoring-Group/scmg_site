from django.shortcuts import render

def home(request):
    return render(request, 'landingapp/home.html')

def about(request):
    return render(request, 'landingapp/about.html')

def map_page(request):
    return render(request, 'landingapp/map.html')


