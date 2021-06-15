# busqueda binaria de x en l, y corta apenas encuentra alguna aparicion de x
def busquedaBinaria(x,l):
	rv = -1
	izq = 0
	der = len(l)-1
	while rv == -1 and izq < der:
		med = (izq+der)/2
		if l[med] == x:
			rv = med
		elif l[med] < x:
			izq = med+1
		else:
			der = med
	return rv

# devuelve el indice de la primera aparicion de x en l[0:der+1]
# pre: l[der]==x
def primeraAparicion(x,l,der):
	izq = 0
	while izq<der:
		med = (izq+der)/2
		if l[med]<x:
			izq = med+1
		else:
			der = med
	return der


# devuelve el indice de la ultima aparicion de x en l[izq:len(l)]
# pre: l[izq]==x
def ultimaAparicion(x,l,izq):
	der = len(l)-1
	while izq<der: 
		med = (izq+der+1)/2
		if l[med]>x:
			der = med-1
		else:
			izq = med
	return der


# devuelve la cantidad de apariciones de x en l
def cantApariciones(x,l):
	rv = 0
	pos = busquedaBinaria(x,l)
	if pos != -1:
		primero = primeraAparicion(x,l,pos)
		ultimo = ultimaAparicion(x,l,pos)
		rv = ultimo-primero+1
	return rv

	
l = [1,1,1,2,2,2,4,4,5,5,6,7,8,9,9,9,9]
print l
for i in range(10):
	print "#("+str(i)+") =", cantApariciones(i,[1,1,1,2,2,2,4,4,5,5,6,7,8,9,9,9,9])

