from Mapa import*
def HP(Sopa,Palabra)
	RV=False
	for pos_inicial in PosEnSopa(Sopa,Palabra[0]):
		RV=RV or HP_pos_inicial(Sopa,Palabra,pos_inicial)
	return RV

def HP_pos_inicial(Sopa,Palabra,pos_inicial):
	if(Palabra.len()==1):
		RV=True
	else:
		RV=False
		escribir(Sopa,pos_inicial,2)
		Palabra_aux=Palabra
		Palabra_aux.remove(Palabra_aux[0])
		for x in PosAlr(Sopa,pos_inicial,Palabra_aux[0]):
			RV=RV or HP_pos_inicial(Sopa,Palabra_aux,x)
	return RV

def escribir(Sopa,pos,x):
	S=open('sopa.txt',r)
	filas_Sopa=Sopa.readlines()
	S.close()
	S=open('sopa.txt',w)
	S


def PosEnSopa(Sopa,x):
#Pre: x in Sopa
	S=open('sopa.txt',r)
	filas_Sopa=Sopa.readlines()
	S.close()
	i=0
	j=0
	pos_x=[]
	while(i<len(filas_sopa)):
		while(j<len(filas_sopa[i])):
			if(filas_sopa[i][j]==x):
				pos_x=pos_x+[[i,j]]
			j=j+1
		i=i+1
	return pos_x
		

def PosAlr(Sopa,pos,Palabra[0]):
	S=open('sopa.txt',r)
	filas_Sopa=Sopa.readlines()
	S.close()


Sopa=open('sopa.txt',r)
