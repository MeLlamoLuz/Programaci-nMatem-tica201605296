# -*- coding: utf-8 -*-
def archivo(cadena):
    nombre = cadena
    nombre = nombre + ".txt"
    archivo = open(nombre,'w')
    codigo = "\documentclass{article}"
    archivo.write(codigo)
    archivo.close()

archivo("hola")