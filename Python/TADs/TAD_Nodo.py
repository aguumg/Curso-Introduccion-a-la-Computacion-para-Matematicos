class Nodo:
#Defino un Nodo con la estructura: Nodo:=<valor:ELEM, izq: Ref(Nodo), der: Ref(Nodo)>

	#Constructor
	def __init__(self, valor):
		self.valor=valor
		self.izq=None
		self.der=None

