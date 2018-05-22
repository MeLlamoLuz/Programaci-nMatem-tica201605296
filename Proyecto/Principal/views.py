# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from .forms import RegexForm
from .models import Regex
from .InfijoAPostFijo import infijoAPostfijo


def RegexView(request):
    if request.method == "POST":
        texto = request.POST.get("textbar")
        result = infijoAPostfijo(texto)
    return render(request, 'Principal.html', {'result': result})