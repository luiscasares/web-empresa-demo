from django.shortcuts import render

# Create your views here.
# Vista genericas del proyecto

def home(request):
    return render (request, 'core/home.html')

def about(request):
    return render (request, 'core/about.html')


def store(request):
    return render (request, 'core/store.html')

def blog(request):
    return render (request, 'core/blog.html')
