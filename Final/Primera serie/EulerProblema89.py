# -*- coding: utf-8 -*-

#Plan/EStrategia:
    #La nota en el enunciado del problema nos ayuda. Dentro del texto podremos encontrar:
        #IIII que se puodría sustituir por IV
        #VIIII que puede sustituirse por IX
        #XXXX es XL
        #LXXXX es XC
        #CCCC es CD
        #DCCCC es CM
    #Con esto podríamos contar los caracteres iniciales en el texto luego los finales y restarlos,
    #o contar los caracteres solamentes de los numeros que sustitumos; que de 5 o 4 caracteres pasan a ser 2 caracteres.
    #También podríamos sustituir los números no minimales por los correctos o sólo por dos caracteres cualquiera
    #porque lo que necesitamos realmente es la cantidad.
    #Entonces tenemos una expresión regular para encontrar lo que reemplazaremos: IIII|VIIII|XXXX|LXXXX|CCCC|DCCCC.

#Iniciamos
import re

#Cargamos el texto
texto = open('p089_roman.txt', 'r')

#Establecemos el patrón o expresión regular:
expresion = 'IIII|XXXX|CCCC|VIIII|LXXXX|DCCCC'

#No sustituiremos por lo correcto
sustitucion = 'SS'

#Iniciamos la cuenta
cuenta = 0

#Realizamos la sustitucion
for numero in texto:
    l = len(numero)
    numero = re.sub(expresion, sustitucion, numero)
    cuenta += l - len(numero)

print "Usando notación minimal se ocupan " + str(cuenta) + " caracteres menos."