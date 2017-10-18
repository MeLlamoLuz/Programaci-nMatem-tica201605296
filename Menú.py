# -*- coding: utf-8 -*-

import requests
import json
from __builtin__ import raw_input

def stateJson():
    states = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ST&limit=52"
    responseStates = requests.get(states , headers={'token': 'yqvvFXHGSiiWaOVyftMWpnbbPOePcRLb'})
    
    statesjson = responseStates.json()
    #print jso
    b = 1
    for a in statesjson["results"] : 
        print ("[" + str(b) + "]"+" "+a.get("name"))
        b =b+1

def getStions(statesStation):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:"+str(statesStation)
    
    response = requests.get(url , headers={'token': 'yqvvFXHGSiiWaOVyftMWpnbbPOePcRLb'})
    jso=response.json()
    print len(jso)
    
    b = 1
    if (len(jso)!=0):
        for a in jso["results"] : 
            print ("[" + str(b) + "]"+" "+a.get("name"))
            b =b+1
    
def allStation():
    i = 0
    for i in range(1,52):
        if (i<10):
            station = "0" + str(i)
        else:
            station = i
        print station
        getStions(station) 


def listarEstacion(estado, estacion):
    if (estado<10):
            station = "0" + str(estado)
    else:
            station = estado
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:"+str(station)
    token = "yqvvFXHGSiiWaOVyftMWpnbbPOePcRLb"
    response = requests.get(url , headers={'token': 'yqvvFXHGSiiWaOVyftMWpnbbPOePcRLb'})
    jso=response.json()
    
    if (len(jso)!=0):
        atributo = jso["results"][estacion]
        imprimir = "name: " + str (atributo ["name"])+ "\nelevation: " + str (atributo ["elevation"]) + "\nmaxdate: " + str (atributo ["maxdate"]) + "\nlongitude: " + str (atributo ["longitude"]) + "\nlatitude: " + str (atributo ["latitude"])  + "\nid: " + str (atributo ["id"]) + "\nmindate: " + str (atributo ["mindate"])
        print imprimir
        return imprimir
        
usuarios = []

def menuDatos():
    opcion = 0

    while True:
        print ("¿A qué deseas acceder?")
        print ("1 - La lista de estados y regiones de EEUU.")
        print ("2 - Las estaciones meteorológicas de los estados y regiones.")
        print ("3 - Las estaciones meteorologicas para un estado en particular.")
        print ("4 - Los datos disponibles  de la estación meteorologica para una estación en particular.")
        print ("5 - Salir")
        opcion = elegirOpcion()
     
        if opcion == 1:
            print stateJson()
            print "Ingrese 0 para continuar"
            elegirOpcion()
        elif opcion == 2:
            print allStation()
            print "Ingrese 0 para continuar"
            elegirOpcion()
        elif opcion == 3:
            station = int(raw_input("Ingresa el n�mero del estado que deseas consultar: "))
            if (station<10):
                station = "0" + str(station)
            else:
                station = station
            print getStions(station)
            print "Ingrese 0 para continuar"
            elegirOpcion()
        elif opcion == 4:
            estado = int(raw_input("Ingresa el número del estado: "))
            estacion = int(raw_input("Ingresa el número de la estación: "))
            print listarEstacion(estado, estacion)
            print "Ingrese 0 para continuar"
            elegirOpcion()
        elif opcion == 5:
            print "1 - Cerrar sesion y salir"
            print "2 - Cerrar sesion sin salir"
            print "3 - No cerrar sesion"
            opcion = elegirOpcion()
            if opcion==1:
                print "Llamar funcion de correo etc"
                print "Llamar funcion para terminar ejecucion"
            elif opcion==2:
                print "Llamar funcion de correo etc"
                MenuPrincipal()
                


def nuevoUsuario():
    usuario = raw_input("Ingresa tu correo: ")
    contrasena = raw_input("Crea tu contraseña: ")
    if usuario.__contains__("@") and( usuario.__contains__(".com") or usuario.__contains__(".es")) :
        usuarioNuevo = [ usuario , contrasena ]
        usuarios.append(usuarioNuevo)
        print "Has creado tu usuario."
        ingresoUsuario()
    else:
        print "Correo invalido"
        nuevoUsuario()
    
def ingresoUsuario():
    usuario = raw_input("Ingresa tu correo: ")
    contrasena = raw_input("Ingresa tu contraseña: ")
    usuarioRegistrado = [ usuario , contrasena ]
    for a in usuarios:
        if usuarioRegistrado == a:
            print "Has ingresado con éxito."
            menuDatos()            
        else:
            print "Datos incorrectas, ingrésalos de nuevo."
            print ingresoUsuario()


def MenuPrincipal():
    salir = False
    opcion = 0
    
    
    while not salir:
     
        print ("Hola.")
        print ("1 - Ingresa a tu cuenta.")
        print ("2 - Crea una cuenta.")
        print ("3 - Salir.")
        
        opcion = elegirOpcion()
     
        if opcion == 1:
            print ingresoUsuario()
        elif opcion == 2:
            print nuevoUsuario()
        elif opcion == 3:
            print ("Adiós.")
        elif opcion == 4:
            salir = True
            
        else:
            print ("Introduce un numero entre 1 y 3")

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

salir = False
opcion = 0


while not salir:
 
    print ("Hola.")
    print ("1 - Ingresa a tu cuenta.")
    print ("2 - Crea una cuenta.")
    print ("3 - Salir.")
    
    opcion = elegirOpcion()
 
    if opcion == 1:
        print ingresoUsuario()
    elif opcion == 2:
        print nuevoUsuario()
    elif opcion == 3:
        print ("Adiós.")
    elif opcion == 4:
        salir = True
        
    else:
        print ("Introduce un numero entre 1 y 3")