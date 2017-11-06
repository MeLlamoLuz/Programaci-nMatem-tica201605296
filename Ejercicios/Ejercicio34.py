def factorial(n):
  if n < 2:
    return 1
  else:
    result = 1
    for i in xrange (2, n + 1):
      result = result * i
    return result

def digitos(n):
    suma = 0
    for x in list(str(n)):
        suma += factorial(int(x))
    return suma
        
numeros = []

for x in xrange(10000001):
    if digitos(x) == x:
        numeros.append(x)
        
suma = 0
for x in numeros:
    suma += int(x)
    
print suma