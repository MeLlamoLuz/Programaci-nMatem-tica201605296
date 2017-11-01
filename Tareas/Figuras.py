# -*- coding: utf-8 -*-

import sys

def rectangulol(b,h):
    for x in range(h):
        print ". "*(b-1) + "."
        
def rectangulov(b,h):
    print ". "*(b-1) + "."
    for x in range(h-2):
        print "." + " "*(2*b-3) + "."
    print ". "*(b-1) + "."
    
def triangulol(b):
    for x in range(1,b+1):
        print (x-1)*". " + "."

def triangulov(b):
    print "."
    for x in range(b-2):
        print ". " + " "*2*x + "."
    print ". "*(b-1) + "."
    
def cuadradol(l):
    for x in range(l):
        print ". "*(l-1) + "."
        
def cuadradov(l):
    print ". "*(l-1) + "."
    for x in range(l-2):
        print "." + " "*(2*l-3) + "."
    print ". "*(l-1) + "."
    
def elegirOpcion():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elige una opción: "))
            correcto=True
        except ValueError:
            print('Error, elige una opción')
     
    return num
def Menu():
    salir = False
    opcion = 0

    while not salir:
 
        print ("Hola. ¿Qué figura deseas hacer?")
        print ("1 - Cuadrado")
        print ("2 - Rectángulo")
        print ("3 - Triángulo equilátero")
        print ("Presiona 4 si deseas salir.")
    
        opcion = elegirOpcion()
 
        if opcion == 1:
            l = int(raw_input("Escribe la medida del lado: "))
            print ("¿Cómo quieres que sea?")
            print ("1 - Relleno")
            print ("2 - Sólo con el borde")
            n = elegirOpcion()
            if n == 1:
                cuadradol(l)
                print ("¿Quieres hacer otra figura?")
                print ("1 - Sí.")
                print ("2 - No.")
                m = elegirOpcion()
                if m == 1:
                    Menu()
                elif m == 2:
                    break
            elif n == 2:
                cuadradov(l)
                print ("¿Quieres hacer otra figura?")
                print ("1 - Sí.")
                print ("2 - No.")
                m = elegirOpcion()
                if m == 1:
                    Menu()
                elif m == 2:
                    break         
        elif opcion == 2:
            b = int(raw_input("Escribe la medida de la base: "))
            h = int(raw_input("Escribe la medida de la altura: "))
            print ("¿Cómo quieres que sea?")
            print ("1 - Relleno")
            print ("2 - Sólo con el borde")
            n = elegirOpcion()
            if n == 1:
                rectangulol(b, h)
                print ("¿Quieres hacer otra figura?")
                print ("1 - Sí.")
                print ("2 - No.")
                m = elegirOpcion()
                if m == 1:
                    Menu()
                elif m == 2:
                    break
            elif n == 2:
                rectangulov(b, h)
                print ("¿Quieres hacer otra figura?")
                print ("1 - Sí.")
                print ("2 - No.")
                m = elegirOpcion()
                if m == 1:
                    Menu()
                elif m == 2:
                    break
        elif opcion == 3:
            b = int(raw_input("Escribe la medida del lado: "))
            print ("¿Cómo quieres que sea?")
            print ("1 - Relleno")
            print ("2 - Sólo con el borde")
            n = elegirOpcion()
            if n == 1:
                triangulol(b)
                print ("¿Quieres hacer otra figura?")
                print ("1 - Sí.")
                print ("2 - No.")
                m = elegirOpcion()
                if m == 1:
                    Menu()
                elif m == 2:
                    break
            elif n == 2:
                triangulov(b)
                print ("¿Quieres hacer otra figura?")
                print ("1 - Sí.")
                print ("2 - No.")
                m = elegirOpcion()
                if m == 1:
                    Menu()
                elif m == 2:
                    break
        elif opcion == 4:
            sys.exit()
        else:
            print ("Introduce un numero entre 1 y 3")

Menu()