from django.shortcuts import render,redirect
from .models import Problem
from onlinejudge.compiler import compile_code, run_code
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
import os
 # Create your views here.

def HomePage(request):
    question = Problem.objects.all()
    return render(request,'home.html',{'questions':question})

 

def problem(request, problem_id):
    question = problem.objects.get(pk=problem_id)
    # print(question.problem_name)
    print(problem_id)
    return render(request,'question.html',{'question':question})

def verdict(request, problem_id):
    question = problem.objects.get(pk=problem_id)
    return render(request, 'verdict.html', {'question': question })