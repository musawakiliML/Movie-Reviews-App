from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse(content='<h1>Hello, Home</h1>')

def about(request):
    return HttpResponse("<h1>Welcome to About us page</h1>")