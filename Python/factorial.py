def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
x=int(input("Ingrese el valor al que le quiere calcular el factorial "))
print('El factorial de ', x, 'es ', fact(x))

