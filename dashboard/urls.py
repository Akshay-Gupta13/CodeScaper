from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.SignupPage, name='signup'),
  path('login/', views.LoginPage, name='login'),
  path('logout/', views.LogoutPage, name='logout'),


]