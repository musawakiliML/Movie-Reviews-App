from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.

# Signup View
def signup(request):
    if request.method == "GET":
        context = {'form': UserCreateForm}
        return render(request, 'signup.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {
                    'form': UserCreateForm,
                    'error': 'Username already taken. Choose new username.' 
                }
                return render(request, 'signup.html', context)
        else:
            context = {
                'form': UserCreateForm,
                'error': 'Passwords do not match'
            }
            return render(request, 'signup.html', context)
            