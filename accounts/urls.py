from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutacc, name='logoutacc'),
    path('login/', views.loginacc, name='loginacc')
]