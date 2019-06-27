from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='home' ),
    path('signup/signup',signup,name='signup'),
    path('home/',profile,name='profile'),
    path('post',post,name='post'),
    path('',login),
    path('login',login),
    path('spe',spe),

]
