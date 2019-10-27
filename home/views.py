from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'home/index.html')


def log(request):
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../auth/',)

        else:
            context = {
                'fail': True
            }
            return render(request, 'home/index.html', context=context)
    return render(request, 'home/index.html')

