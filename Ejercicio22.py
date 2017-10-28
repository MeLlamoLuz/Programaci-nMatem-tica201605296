# -*- coding utf-8 -*-

f1 = open('46k.txt', 'r')
for line in f1:
    f1.write(line.replace('""', ''))
f1.close()

nombres = open('46.txt', 'r')
for line in nombres.readlines():
    nombres = line.split(",")
    nombres.sort()

def punteoNombre(nombre):
    letras = [ord(x)-64 for x in list(nombre)]
    return sum(letras)

total = 0

for x in xrange(len(nombres)):
    total = total +punteoNombre(nombres[x])*(x+1)
    
print total