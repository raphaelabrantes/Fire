from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuarios, Administrador
from .forms import Admin_form
from ipaddress import IPv4Address
from hashlib import md5

@login_required(login_url='/home')
def suck(request):
    users = Usuarios.objects.order_by('-date_add')
    adms = Administrador.objects.order_by('-date')
    list_adms = []
    list_users = []
    for x in adms:
        name = x.name
        list_adms.append(name)
    for i in users:
        ip = str(IPv4Address(i.ip))
        name = i.name
        list_users.append([name, ip])
    context = {
        'users': list_users,
        'forms': Admin_form(),
        'adms': list_adms,
    }
    return render(request, 'menu/menu.html', context=context)

@login_required(login_url='/home')
def logout_click(request):
    logout(request)
    return redirect('../home')

@login_required(login_url='/home')
def add_adm(request):
    if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_superuser(username=username,
                                 email=email,
                                 password=password)
        hexx = md5(password.encode()).hexdigest()
        adm = Administrador(name=username, password=hexx)
        user.save()
        adm.save()
    return redirect('../')