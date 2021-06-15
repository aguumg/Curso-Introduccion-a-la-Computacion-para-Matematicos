# implementacion del TAD casillero
class Casillero:
	
	# crea un nuevo casillero con letra l
	def __init__(self, l):
		self.letra = l
		self.marca = False

	# devuelve la letra del casillero
	def verLetra(self):
		return self.letra

	# marca el casillero como visitado
	def marcar(self):
		self.marca = True

	# desmarca el casillero
	def desmarcar(self):
		self.marca = False

	# devuelve True sii el casillero esta marcado
	def estaMarcado(self):
		return self.marca

	# para imprimir casilleros
	def __repr__(self):
		return self.letra

# implementacion del TAD Grilla
class Grilla:
	
	# asume que llc es una lista de de listas de Casilleros
	# Alternativamente, se podría permitir leer un archivo y transformar cada letra a un objeto Casillero
	def __init__(self, llc):
		self.casilleros = llc

	# devuelve el casillero que esta arriba de c o None si no tiene ninguno	
	def superior(self, c):
		rv = None
		pos = self.obtenerPosicion(c)
		if pos != None and pos[0] != 0:
			rv = self.casilleros[pos[0]-1][pos[1]] 
		return rv
	
	# devuelve el casillero que esta abajo de c o None si no tiene ninguno	
	def inferior(self, c):
		rv = None
		pos = self.obtenerPosicion(c)
		if pos != None and pos[0] != len(self.casilleros)-1:
			rv = self.casilleros[pos[0]+1][pos[1]] 
		return rv

	# devuelve el casillero que esta a la derecha de c o None si no tiene ninguno	
	def derecho(self, c):
		rv = None
		pos = self.obtenerPosicion(c)
		if pos != None and pos[1] != len(self.casilleros[0])-1:
			rv = self.casilleros[pos[0]][pos[1]+1] 
		return rv

	# devuelve el casillero que esta a la izquierda de c o None si no tiene ninguno	
	def izquierdo(self, c):
		rv = None
		pos = self.obtenerPosicion(c)
		if pos != None and pos[1] != 0:
			return self.casilleros[pos[0]][pos[1]-1] 
		return rv

	# devuelve una lista con todos los casilleros de la grilla
	def obtenerCasilleros(self):
		rv = []
		for fila in self.casilleros:
			rv = rv + fila
		return rv

	# devuelve el par (i,j) correspondiente a c, o None si no es parte del tablero
	def obtenerPosicion(self, c):
		rv = None
		for fila in range(len(self.casilleros)):
			for columna in range(len(self.casilleros[fila])):
				if self.casilleros[fila][columna] == c: #no compara por igualdad observacional, compara que sean el mismo objeto, es decir su posicion de memoria
					rv = (fila,columna)
		return rv #No es una buena forma de modelar el problema de asociar una posicion con el casillero

	# devuelve el string para imprimir una grilla por pantalla
	def __str__(self):
		rv = ""
		for fila in self.casilleros:
			rv = rv + str(fila) + "\n"
		return rv
