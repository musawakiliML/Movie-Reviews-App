from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Signup View
def signup(request):
    context = {'form': UserCreationForm}
    return render(request, 'signup.html', context)