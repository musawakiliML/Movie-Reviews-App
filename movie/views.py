from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Movie

# Create your views here.


def home(request):
    searchTerm = request.GET.get("searchMovie")
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    
    context = {
        "searchTerm": searchTerm,
        "movies": movies
    }
    return render(request, 'home.html', context)


def about(request):
    return HttpResponse("<h1>Welcome to About us page</h1>")


def signup(request):
    email = request.GET.get('email')

    context = {
        "email": email
    }
    return render(request, 'signup.html', context)
