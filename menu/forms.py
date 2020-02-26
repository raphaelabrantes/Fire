from django import forms
from menu.models import Usuarios
from ipaddress import IPv4Address

class Admin_form(forms.Form):
    username = forms.CharField(label='username', max_length=18)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class User_form(forms.Form):
    name = forms.CharField(label='username', max_length=35)
    ip = forms.GenericIPAddressField(label='ip', unpack_ipv4=True)

class Port_forms(forms.Form):
    ip_list = [(user.pk, IPv4Address(user.pk)) for user in Usuarios.objects.all()]
    ip_select = forms.ChoiceField(choices=ip_list)
    port = forms.IntegerField(max_value=65535, min_value=0)