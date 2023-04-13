from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm

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

def movie(request):
    return HttpResponse("<h1>Movies Page</h1>")

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie':movie
    }
    return render(request, 'detail.html', context)

def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "GET":
        context = {
            'form': ReviewForm,
            'movie': movie
        }
        return render(request, 'createreview.html', context)
    else:
        try:
            form = ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            
            return redirect('detail', new_review.movie.id)
        except ValueError:
            context = {
                'form':ReviewForm,
                'error': 'bad data passed in'
            }
            return render(request, 'createreview.html', context)