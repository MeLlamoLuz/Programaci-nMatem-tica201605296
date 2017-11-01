def esPrimo(a):
    return not (a<2 or any (a % i == 0 for i in range(2, int(a**0.5)+1)))

def permutacionCircular(x):
    s = str(x)
    return [s[n:] + s[:n] for n in range(1, len(s))]

primos = []

for x in range(1000001):
    if esPrimo(x) == True:
        primos.append(x)

primosc = []

for x in primos:
    s = permutacionCircular(x)
    if all([esPrimo(int(y))==True for y in s])==True:
           primosc.append(x)

print len(primosc)