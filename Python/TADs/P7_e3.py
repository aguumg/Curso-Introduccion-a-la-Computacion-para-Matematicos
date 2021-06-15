from TAD_ArbolBinario import*

def Max(A):
#Caso base: A es una hoja
	if(not A.HayIzq() and not A.HayDer()):
		RV=A.Raiz()
	else:
		if(not A.HayIzq()):
			RV=max(A.Raiz(),Max(A.Der()))
		elif(not A.HayDer()):
			RV=max(A.Raiz(),Max(A.Izq()))
		else:
			RV=max(A.Raiz(),Max(A.Izq()),Max(A.Der()))
	return RV

A=ArbolBinario(3)
A.AgregarIzq(15)
A.AgregarDer(155)
A.AgregarIzq(30)
print(Max(A))

