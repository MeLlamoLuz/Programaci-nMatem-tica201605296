# -*- coding: utf-8 -*-

from django.db import models

class Usuario(models.Model):
    Apellidos = models.CharField(max_length = 20)
    Nombres = models.CharField(max_length = 20)
    Correo = models.CharField(max_length = 20)
    CUI = models.CharField(max_length = 20)
    Carreras = (('M', 'Matematica'),('F', 'Fisica'))
    Carrera = models.CharField(max_length = 10, choices = Carreras, default='M')
    
    def NombreCompleto(self):
        cadena = "{0}, {1}"
        return cadena.format(self.Apellidos, self.Nombres)
     
    def __str__(self):
        return self.NombreCompleto()
