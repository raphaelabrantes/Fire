from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

@login_required(login_url='/home')
def suck(request):
    return HttpResponse("vai")
