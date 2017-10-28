# -*- coding: utf-8 -*-

ListadePrimos = []

def esPrimo(a):
    return not (a<2 or any (a % i == 0 for i in range(2, int(a**0.5)+1)))

for x in range(110000):
    if esPrimo(x) == True:
        ListadePrimos.append(x)

print ListadePrimos[10000]