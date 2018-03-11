# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class UserFormView(View):
    forrm_class = UserForm
    template_name = '/registro.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commmit=False)
            
            username =  form.cleanned_data['Nombre']
            password =  form.cleanned_data['Contraseña']
            user.set_password(password)
            user.save()
            
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('perfil')
            
        return render(request, self.template_name, {'form': form})
                 
                                     
            
        