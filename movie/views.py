from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def HomeView(request):
    return HttpResponse(content='<h1>Hello, Home</h1>')
