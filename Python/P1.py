x=list(input("Ingrese la lista "))
i=0
j=1
a=[0]
b=[0]
while(i<=len(x)-2):
    if(x[i]==x[i+1]):
        j=j+1
        b.append(x[i])
        a.append(j)
    else:
        j=1
    i=i+1
print('La longitud de la meseta mas larga es: ', max(a), '\n', 'Y el numero de la meseta mas larga es :', b[a.index(max(a))])
