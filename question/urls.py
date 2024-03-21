from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('problem/<int:problem_id>',views.ProblemPage,name='problem'),
    path('problem/<int:problem_id>/verdict',views.verdict, name='verdict'),
    path('submissions',views.sub, name='submissions'),
    path('problem/customTc', views.customTc, name='customTc'),
]