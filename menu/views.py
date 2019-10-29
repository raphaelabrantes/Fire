from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='/home')
def suck(request):
    return render(request, 'menu/menu.html')

@login_required(login_url='/home')
def logout_click(request):
    logout(request)
    return redirect('../home')

