from django.shortcuts import render,redirect
from .models import Problem, test_case
from onlinejudge.compiler import CodeCompiler, codeExecute
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from pathlib import Path

import json
from django.http import JsonResponse

import os
 # Create your views here.

def HomePage(request):
    question = Problem.objects.all()
    return render(request,'home.html',{'question':question})

#############################################################

def ProblemPage(request, problem_id):
    question = Problem.objects.get(pk=problem_id)
    # print(question.problem_name)
    # print(problem_id)
    return render(request,'question.html',{'question':question})
#############################################################

def verdict(request, problem_id):
    question = Problem.objects.get(pk=problem_id)
    return render(request, 'verdict.html', {'question': question })
#############################################################
