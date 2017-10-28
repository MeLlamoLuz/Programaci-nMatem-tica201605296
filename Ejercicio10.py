# -*- coding: utf-8 -*-

Primos = []
suma = 0

def esPrimo(a):
    return not (a<2 or any (a % i == 0 for i in range(2, int(a**0.5)+1)))

for x in range(2000001):
    if esPrimo(x) == True:
        suma = suma + x

print suma