from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    newss = News.objects.all()
    
    context = {
        "newss": newss
    }
    
    return render(request, 'news.html', context)