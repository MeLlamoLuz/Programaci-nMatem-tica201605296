# -*- coding: utf-8 -*-

#Empezamos definiendo la clase del autómata.
class Automata:

    def __init__(self, no_estados):
        #Creamos una lista con "listitas" con el número de "transiciones" o movimientos que hay en el AFD.
        self.transiciones = [{} for i in range(no_estados)]
        #Iniciamos suponiendo que ningún estado es de aceptación, entonces que cualquier cadena ingresada no es divisible entre 2.
        self.estadosAceptacion = ["es impar."] * no_estados

    #Esta es la función de transición. En la lista de transiciones que creamos inicialmente, ingresamos las transiciones. Cada elemento del alfabeto con su respectivo estado.
    def T(self, estadoActual, alf, estadoSiguiente):
        self.transiciones[estadoActual][alf] = estadoSiguiente

    #Reemplazamos, en la lista establecida al inicio, en la posición del estado de aceptación, en el que se aceptan los números pares:
    def EstadoDeAceptacion(self, estado):
        self.estadosAceptacion[estado] = "es par."

    #Con esta función vemos el movimiento de la cadena a través del autómota caracter por caracter.
    def Movimiento(self, cadena):
        estado = 0
        try:
            for alf in cadena:
                estado = self.transiciones[estado][alf]
            return cadena + " " + self.estadosAceptacion[estado]
        except KeyError:
            return False

afd = Automata(3)
#Enlistamos las transiciones posibles con el autómata
afd.T(0, '0', 1)
afd.T(0, '1', 2)
afd.T(1, '0', 1)
afd.T(1, '1', 2)
afd.T(2, '0', 1)
afd.T(2, '1', 2)
afd.EstadoDeAceptacion(1)

#Ingresamos cadenas
print afd.Movimiento('10')  #Par
print afd.Movimiento('0110')  #Par
print afd.Movimiento('111')  #Impar
print afd.Movimiento('0101')  #Impar