from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
  path('', views.SignupPage, name="signup"),
  path('login/', views.LoginPage, name="login"),
  path('home/', views.HomePage, name="home"),
  path('logout/', views.LogoutPage, name="logout"),


]