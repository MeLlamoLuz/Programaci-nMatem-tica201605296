# -*- coding: utf-8 -*-

from django.shortcuts import render
from .InfijoAPostFijo import infijoAPostfijo

def RegexView(request):
    if request.method == "POST":
        textbar = request.POST.get("texto")
        respuesta = infijoAPostfijo(textbar)
        return render(request, 'Principal.html', {'result': respuesta})
    return render(request, 'Principal.html')

