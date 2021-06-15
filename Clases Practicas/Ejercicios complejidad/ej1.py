import time

# busqueda lineal de x en l
def busquedaLineal(x,l):
	rv = -1
	i = 0
	while i < len(l):
		if l[i] == x:
			rv = i
		i = i+1
	return rv

# busqueda binaria de x en l
def busquedaBinaria(x,l):
	rv = -1
	izq = 0
	der = len(l)-1
	while izq < der:
		med = (izq+der)/2
		if l[med] < x:
			izq = med+1
		else:
			der = med
	if l[izq] == x:
		rv = izq
	return rv

# comparacion de tiempos de ejecucion entre ambas busquedas
print "Busquedas sobre 41.450.000 (poblacion argentina aprox.)"
print "Iniciando busqueda lineal..."
t0 = time.clock()
busquedaLineal(745,range(41450000))
tiempo = time.clock() - t0
print "Busqueda lineal:", round(tiempo,2), "seg."

print "Iniciando busqueda binaria..."
t0 = time.clock()
busquedaBinaria(745,range(41450000))
tiempo = time.clock() - t0
print "Busqueda binaria:", round(tiempo,2), "seg."

