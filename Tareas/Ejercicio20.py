# -*- coding: utf-8 -*-

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
        
suma = 0

for i in str(factorial(100)):
    suma = suma + int(i)
    
print suma