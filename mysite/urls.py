from django.urls import path, include, re_path

from . import views
from authors import views as auth_view

urlpatterns = [
    path('', views.homepage, name='home'),
    path('posts/', views.posts, name='posts'),
    path('contacts/', views.contacts, name='contacts'),
    #path('login/', views.login, name='login'),
    re_path(r'^login/', include([
        re_path(r'^$', views.login_user, name='login'),
        #re_path(r'^author/$', auth_view.author_home, name='login_author'),
        re_path(r'^author/', include('authors.urls')),
        re_path(r'^approver/', views.login, name='login_approver'),
    ])),
    path('register/', views.register, name='register'),
]