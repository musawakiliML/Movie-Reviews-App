from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
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
    reviews = Review.objects.filter(movie = movie)

    context = {
        'movie':movie,
        'reviews':reviews
    }
    return render(request, 'detail.html', context)

@login_required
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

@login_required
def updatereview(request, review_id):
    '''Function to create update review view'''
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request == 'GET':
        form = ReviewForm(instance=review)
        context = {
            'review':review,
            'form':form
        }
        return render(request, 'updatereview.html', context)
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            context = {
                'review':review,
                'form':form,
                'error':'Bad data in form'
            }
            return render(request, 'updatereview.html', context)

@login_required
def deletereview(request, review_id):
    '''This function deletes the review'''
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)