from os import system
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Usuarios, Portas
from .forms import Admin_form, User_form, Port_forms
from ipaddress import IPv4Address

@login_required(login_url='/home')
def suck(request):
    users = Usuarios.objects.order_by('-date_add')
    adms = User.objects.order_by('-date_joined')
    portas = Portas.objects.order_by('-date_add')
    list_adms = [x.username for x in adms]
    list_users = []
    list_ports = []
    for i in users:
        ip = str(IPv4Address(i.ip))
        name = i.name
        list_users.append([name, ip])
    for p in portas:
        port = p.port
        date_add = p.date_add
        ip = str(IPv4Address(p.ip.ip))
        name = p.ip.name
        list_ports.append([name, port, ip, date_add])
    uniq_usr = list(set([name for name, ip in list_users]))
    context = {
        'users': list_users,
        'admin_forms': Admin_form(),
        'adms': list_adms,
        'user_forms': User_form(),
        'portas': list_ports,
        'user_u': uniq_usr,
        'port_form': Port_forms(),
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

@login_required(login_url='/home')
def delete_user(request):
    if 'user_name' in request.POST:
        ips = [user for user in Usuarios.objects.filter(name=request.POST['user_name'])]
        for user in ips:
            for p in Portas.objects.filter(ip=user):
                command = "ufw delete allow from {} to any port {}".format(str(IPv4Address(user.ip)), p.port)
                system(command)
                p.delete()
            user.delete()
    return redirect('../')

@login_required(login_url='/home')
def add_port(request):
    if 'ip_select' in request.POST and 'port' in request.POST:
        ip = request.POST['ip_select']
        port = request.POST['port']
        new_port = Portas(ip=Usuarios.objects.get(ip=ip), port=port)
        command = "ufw allow from {} to any port {} ".format(str(IPv4Address(int(ip))), port)
        system(command)
        new_port.save()
    return redirect('../')