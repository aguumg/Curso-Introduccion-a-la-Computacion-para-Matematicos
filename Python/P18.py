x=list(input("Ingrese la lista "))
i=0
j=1
a=[0]
b=[0]
while(i<=len(x)-2):
    if(x[i]==x[i+1]):
        j=j+1
        b.append(x[i])      # Uso dos listas auxiliares a y b, para guardar los valores de la meseta y del numero en la meseta
        a.append(j)
    else:
        j=1
    i=i+1
print('La longitud de la meseta mas larga es: ', max(a), '\n', 'Y el numero de la meseta mas larga es :', b[a.index(max(a))])
#Notar que como a a y b les voy agregando cosas al mismo tiempo, entonces tienen los indices iguales, es decir,
#la meseta mas larga sera el maximo valor de a, y el corresondiente numero sera b en la posicion del maximo valor de a.
