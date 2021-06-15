class Pila:

	# Constructor
	def __init__(self):
		self.elems = []

	# Pone x en el tope de la pila
	def apilar(self, x):
		self.elems.append(x)

	# True sii la pila no tiene elementos
	def vacia(self):
		return len(self.elems)==0

	# Devuelve el elemento que esta en el tope de la pila
	# PRE: la pila no esta vacia
	def tope(self):
		return self.elems[len(self.elems)-1]

	# Saca de la pila el elemento que esta en el tope
	# PRE: la pila no esta vacia
	def desapilar(self):
		self.elems.pop()
