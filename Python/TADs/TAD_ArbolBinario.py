from TAD_Nodo import*

class ArbolBinario:
#Estructura de representacion del TAD: 
#	ArbolBinario:=<primero: Ref(TNodo)>
#	Nodo:=<valor:Z, izq: Ref(TNodo), der: Ref(TNodo)>	

	#Constructor
	#Crea un arbol binario con primero=valor
	def __init__(self, valor):
		self.primero=Nodo(valor)

	def Raiz(self):
	#Devuelve el entero almacenado en la raiz del AB A.
		return self.primero.valor

	def HayIzq(self):
	#Dice si el AB tiene subarbol izq.
		return self.primero.izq!=None

	def HayDer(self):
	#Dice si el AB tiene subarbol der.
		return self.primero.der!=None

	def Izq(self):
	#Pre: A.HayIzq()
	#Devuelve el subarbol izq.
		B=ArbolBinario(1)
		B.primero=self.primero.izq
		return B

	def Der(self):
	#Pre: A.HayDer()
	#Devuelve el subarbol der.
		B=ArbolBinario(1)
		B.primero=self.primero.der
		return B

	def AgregarIzq(self, valor):
	#Agrega un nodo(valor) en una nueva rama izq.
		nodo_aux=self.primero
		while(nodo_aux.izq!=None):
			nodo_aux=nodo_aux.izq
		nodo_aux.izq=Nodo(valor)					#Notar que al cambiar nodo_aux se cambiar self. Porque nodo_aux=self.primero no es una copia del noso sino que es una REFERENCIA del nodo de mi arbol, o sea que cuando lo modifique se va a modificar mi arbol.

	def AgregarDer(self, valor):
	#Agrega un nodo(valor) en una nueva rama der.
		nodo_aux=self.primero
		while(nodo_aux.der!=None):
			nodo_aux=nodo_aux.der
		nodo_aux.der=Nodo(valor)
		
