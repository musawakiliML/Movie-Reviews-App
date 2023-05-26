from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    #path('movie/', movie, name='movie'),
    path('<int:movie_id>', detail, name='detail'),
    path('<int:movie_id>/create', createreview, name='createreview'),
    path('review/<int:review_id>', updatereview, name='updatereview'),
    path('review/<int:review_id>/delete', deletereview, name='deletereview')   
]