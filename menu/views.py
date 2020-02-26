from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Usuarios
from .forms import Admin_form, User_form
from ipaddress import IPv4Address

@login_required(login_url='/home')
def suck(request):
    users = Usuarios.objects.order_by('-date_add')
    adms = User.objects.order_by('-date_joined')
    list_adms = []
    list_users = []
    for x in adms:
        name = x.username
        list_adms.append(name)
    for i in users:
        ip = str(IPv4Address(i.ip))
        name = i.name
        list_users.append([name, ip])
    context = {
        'users': list_users,
        'admin_forms': Admin_form(),
        'adms': list_adms,
        'user_forms': User_form(),
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
        user.save()
    return redirect('../')

@login_required(login_url='/home')
def add_user(request):
    if 'name' in request.POST and 'ip' in request.POST:
        name = request.POST['name']
        ip = int(IPv4Address(str(request.POST['ip'])))
        new_user = Usuarios(name=name, ip=ip)
        new_user.save()
    return redirect('../')

@login_required(login_url='/home')
def delete_admin(request):
    if 'admin_name' in request.POST:
        admin_object = User.objects.filter(username=request.POST['admin_name'])
        admin_object.delete()
    return redirect('../')