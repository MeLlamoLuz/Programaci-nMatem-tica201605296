# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
from django.shortcuts import render
from django.views.generic import TemplateView
from collections import defaultdict
import os
ubicacionlatex='automata.tex'

Operadores={'+', '?', '*', '|', '.'}
Parentesis={'(',')'}

Problematicos={'+', '?', '*', '|'}
Unarios={'+', '?', '*'}
temporal=''
newtexto=''
error=0
numeroEstados=0
symbolos=[]
estados_aceptacion=[]
noEstadosAc=0
fThompson=[]
Estados=[]
estadoInicial=0
funcionfinal=[]

def normales(caracter):
    global temporal
    global newtexto
    global error
    if caracter not in Operadores:
        if temporal=='':
            newtexto=newtexto+caracter
            temporal='.'
        else:
            newtexto=newtexto+caracter+'.'
            temporal='.'
    elif caracter in Unarios:
        if temporal in Problematicos:
            error=1
        elif temporal=='.':
            if newtexto[-1]=='.':
                newtexto=newtexto[:-1]
                newtexto=newtexto+caracter+'.'
                temporal=caracter
            else:
                newtexto=newtexto+caracter

def convertidor(texto):
    global temporal
    global newtexto
    temporal2=0
    temporal=""
    ora=0
    newtexto=''
    contador_parentesis_iz=0
    agregador=0
    for caracter in texto:
        if temporal2>0:
            if agregador>0:
                if newtexto[-1]=='.':
                    newtexto=newtexto[:-1]
                    if caracter in Unarios:
                        newtexto=newtexto+'|'+caracter
                    else:
                        newtexto=newtexto+'|'+caracter+'.'
                    agregador-=1
                    temporal2-=1
                else:
                    if caracter in Unarios:
                        newtexto=newtexto+'|'+caracter
                    else:
                        newtexto=newtexto+'|'+caracter+'.'
                    agregador-=1
                    temporal2-=1
            elif caracter in Unarios:
                    newtexto=newtexto+caracter
                    temporal2-=1
                    temporal=''
            else:
                    newtexto=newtexto+caracter+"."
                    temporal=''
                    temporal2-=1
        elif caracter=='|':
            if contador_parentesis_iz>0:
                agregador+=1
            elif ora==0:
                temporal=''
                ora=1
            else:
                temporal=''
                newtexto=newtexto+'|'
        elif caracter=='(':
            temporal=''
            contador_parentesis_iz+=1
        elif caracter==')':
            temporal='.'
            contador_parentesis_iz-=1
            temporal2+=1
        else:
            normales(caracter)
    if ora==1:
        newtexto=newtexto +'|'
    if texto[1] in Operadores:
        error=1
    elif contador_parentesis_iz!=0:
        error=1
    if temporal2>0:
            if agregador>0:
                if newtexto[-1]=='.':
                    newtexto=newtexto[:-1]
                    newtexto=newtexto+'|'
                    agregador-=1
                    temporal2-=1
                else:
                    newtexto=newtexto+'|'
                    agregador-=1
                    temporal2-=1
    return newtexto