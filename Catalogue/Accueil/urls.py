from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.accueil, name='Accueil'),
    path('search/', views.search, name='Search'),
    path('login/', auth_views.LoginView.as_view(next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
