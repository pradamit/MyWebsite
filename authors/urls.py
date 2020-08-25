from django.contrib import admin
from django.urls import path, include
from . import views as auth_views

urlpatterns = [
    path('', auth_views.author_home, name='auth_home'),
    path('logout/', auth_views.author_logout, name='author_logout')
]