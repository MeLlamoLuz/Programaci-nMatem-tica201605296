def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def digitos(n):
    suma = 0
    for x in list(str(n)):
        suma += factorial(int(x))
        
numeros = []

for x in range():
    if digitos(x) == x:
        numeros.append(x)
        
suma = 0
for x in numeros:
    suma += int(x)
    
print suma