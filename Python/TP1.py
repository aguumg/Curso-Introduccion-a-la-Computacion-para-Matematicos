import sys

def esPrimo(n):
    i=2
    while (i<n):
        if(n%i==0):
            return False
        i=i+1
    return True

def cantidadPrimosMenoresOIguales(n):
    i=2
    j=0
    while (i<=n):
        if(esPrimo(i)==True):
            j=j+1
        i=i+1
    return j

def cantidadDivisoresPrimos(n):
    i=2
    j=0
    while(i<=n):
        if(esPrimo(i)==True):
            if(n%i==0):
                j=j+1
        i=i+1
    return j


def iesimoDivisorPrimo(n, i):
    j=2
    k=0
    a={}
    if(i<=cantidadDivisoresPrimos(n)):
        while(j<=n):
            if(esPrimo(j)==True):
                if(n%j==0):
                    a[k]=j
                    k=k+1
            j=j+1
        return a[i-1]
    return -1


def potencia(x, y):
    n=1
    while (y!=0):
        n=n*x
        y=y-1
    return n

def potenciaIesimoDivisorPrimo(n, i):
    j=1
    if(i<=cantidadDivisoresPrimos(n)):
        while(n%potencia(iesimoDivisorPrimo(n, i),j)==0):
            j=j+1
        return j-1
    return -1

print(esPrimo(10))
print(cantidadPrimosMenoresOIguales(10))
print(cantidadDivisoresPrimos(10))
print(iesimoDivisorPrimo(10,2))
print(potenciaIesimoDivisorPrimo(10,2))
