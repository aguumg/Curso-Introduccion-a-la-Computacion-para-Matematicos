from grilla import *

# devuelve True sii p esta en g (resuelve el ejercicio)
def sopaDeLetras(g, p):
	rv = False
	casilleros = g.obtenerCasilleros()
	for c in casilleros:
		if hayPalabraDesde(g,c,p):
			rv = True
	return rv

# devuelve True sii p esta en g y comienza en c
def hayPalabraDesde(g, c, p):
	rv = False
	if len(p) == 0: # Notar que acá todavía ni chequeo que este c sea efectivamente un casillero (vs. None, que es lo que tira si nos fuimos de la grilla)
		rv = True
	else:
		if not c is None and not c.estaMarcado() and p[0] == c.verLetra():
			c.marcar()
			rv = rv or hayPalabraDesde(g, g.superior(c), p[1:len(p)]) 
			rv = rv or hayPalabraDesde(g, g.inferior(c), p[1:len(p)]) 
			rv = rv or hayPalabraDesde(g, g.derecho(c), p[1:len(p)]) 
			rv = rv or hayPalabraDesde(g, g.izquierdo(c), p[1:len(p)])
			c.desmarcar()
	return rv


# ejemplo de uso
casilleros =  []
casilleros.append([Casillero('a'), Casillero('l'), Casillero('d'), Casillero('r')])
casilleros.append([Casillero('q'), Casillero('r'), Casillero('y'), Casillero('e')])
casilleros.append([Casillero('i'), Casillero('s'), Casillero('l'), Casillero('a')])
casilleros.append([Casillero('f'), Casillero('o'), Casillero('t'), Casillero('e')])

g = Grilla(casilleros)
print ("Grilla")
print (g)
print ("sopaDeLetras(g, 'alto'): ", sopaDeLetras(g, 'alto'))
print ("sopaDeLetras(g, 'dibujo'): ", sopaDeLetras(g, 'dibujo'))
print ("sopaDeLetras(g, 'real'): ", sopaDeLetras(g, 'real'))
print ("")
 
