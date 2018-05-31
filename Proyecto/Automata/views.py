# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from Funciones import *


def ExpresionView(request):
    if request.method == "POST":
        expresion = request.POST.get("regex")
        afndObj = regexAafnd(expresion)
        afnd = afndObj.obtenerAFND()
        afdObj = AFNDaAFD(afnd)
        afd = afdObj.obtenerAFD()
        regex = "Expresion regular: " + expresion
        resultado1 = "Automata finito no determinista:"
        lenguaje1 = afnd.desplegarLenguaje()
        estados1 = afnd.desplegarEstados()
        estadoI1 = afnd.desplegarEstInicial()
        estadosA1 = afnd.desplegarEstAceptacion()
        transiciones1= afnd.desplegarTransiciones()
        resultado2 = "Automata finito determinista:"
        lenguaje2 = afd.desplegarLenguaje()
        estados2 = afd.desplegarEstados()
        estadoI2 = afd.desplegarEstInicial()
        estadosA2 = afd.desplegarEstAceptacion()
        transiciones2 = afd.desplegarTransiciones()
        #dibujarGrafoD(afnd, "afnd")
        dibujarLatex(expresion, afnd, "1")
        #dibujarGrafoD(afd, "afd")
        dibujarLatex(expresion, afd, "2")
        latex1 = codigoLatex(expresion, afnd)
        graph1 = afnd.codigoDot()
        latex2 = codigoLatex(expresion, afd)
        graph2 = afd.codigoDot()
        texto1 = "Codigo LaTex"
        texto2 = "Codigo Graphviz"
        texto3 = "Codigo LaTex"
        texto4 = "Codigo Graphviz"
        return render(request, 'Expresion.html', {'texto4': texto4, 'texto2': texto2, 'graph1': graph1, 'graph2': graph2, 'texto1': texto1, 'texto3': texto3, 'latex1': latex1, 'latex2': latex2, 'expresion': regex, 'afnd': resultado1, 'lenguaje1': lenguaje1, 'estados1': estados1, 'estadoinicial1': estadoI1, 'estadosaceptacion1': estadosA1, 'transiciones1':transiciones1, 'afd': resultado2, 'lenguaje2': lenguaje2, 'estados2': estados2, 'estadoinicial2': estadoI2, 'estadosaceptacion2': estadosA2, 'transiciones2':transiciones2})
    return render(request, 'Expresion.html')

#<a href="{{ latex1 }}">{{texto1}}</a>
 #   <a href="{{ graph1 }}">{{texto2}}</a>
#<a href="{{ latex2 }}">{{texto3}}</a>
 #   <a href="{{ graph2 }}">{{texto4}}</a>

