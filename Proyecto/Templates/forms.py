# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['Apellidos','Nombre', 'Correo', 'CUI', 'Carrera', 'Contrase�a']