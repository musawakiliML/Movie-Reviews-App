from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    #path('movie/', movie, name='movie'),
    path('<int:movie_id>', detail, name='detail')
]