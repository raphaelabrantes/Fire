from django import forms

class Admin_form(forms.Form):
    username = forms.CharField(label='username', max_length=18)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class User_form(forms.Form):
    name = forms.CharField(label='username', max_length=35)
    ip = forms.GenericIPAddressField(label='ip', unpack_ipv4=True)
