import sys

# No funca bien y no encuentro el error:
def quitar_barra_n(lista):                              #Esto es porque cada salto de renglon se lee como \n al final de la linea, y eso no lo queremos en la lista, asi que lo borramos. (De las listas que lo tienen, porque list.remove nos tira error si no hay nada)
        if('\n' in lista):                      
                lista.remove('\n')
        return lista

def es_mapa(archivo):
	mapa=open(archivo, 'r')
	lista=mapa.readlines() #esto es una lista cuyo i-esimo lugar es la (i-1)-esima fila del mapa terminando con un '\n' adicional
	longitud=len(quitar_barra_n(list(lista[0])))
	k=0
	i=0
	while i<len(lista): #recorre las posiciones de la lista y si alguna no tiene la longitud correcta o no representa una fila con unicamente 0's y 1's, se incrementa el valor de k.
		if len(quitar_barra_n(list(lista[i])))!= longitud:
			k=k+1
		else:
			j=0
			while j<longitud-1: #le resto 1 porque el string de cada posicion de la lista termina con un '\n', que no hay que considerar.
				if lista[i][j]!='0' or lista[i][j]!='1':
					k=k+1
				j=j+1
		i=i+1
	return k==0 #retorna True si y sólo si nunca incrementé el k (o sea, el archivo representa un mapa)


###########


def cantidad_paredes(archivo):
	mapa=open(archivo,'r')
	lista=mapa.readlines()
	paredes=0
	i=0
	while i<len(lista):
		contador=lista[i].count('1')
		paredes=paredes+contador
		i=i+1
	return paredes



def dimensiones(archivo):
	mapa=open(archivo,'r')
	lista=mapa.readlines()
	alto=len(lista)
	ancho=len(lista[0])-1 #resto 1 porque lista[0] termina con el '\n'
	return alto, ancho



def corredor_horizontal(archivo):
	mapa=open(archivo,'r')
	lista = mapa.readlines()
	maximo=0 #longitud corredor maximo
	i=0
	while i<len(lista): #recorrer las filas del mapa es recorrer cada posicion de la lista (módulo '\n'). Asi que hablo de FILA, en vez de POSICION.
		aux=0 #longitud de un corredor auxiliar en esta fila
		maxfila=0 #longitud del "corredor maximo" de esta fila
		j=0
		while j<len(lista[i]): 
			if lista[i][j]=='0': #cada vez que me paro en un 0, se incrementa la longitud del corredor auxiliar, y la guardo como la longitud maxima de     					    la fila (o sea, 'maxfila'). Esto sucede hasta que, o bien llego a una posicion con un 1 (o al '\n'), o bien termina la fila
				aux=aux+1
				maxfila=aux
			else:		#si me paro en un 1, en este caso reinicio 'aux', y actualizo 'maxfila' (para que sea el maximo de esta fila)
				if maxfila<=aux: 
					maxfila=aux
					aux=0
				else:
					aux=0
			j=j+1
		if maxfila>=maximo:   #esto compara el corredor maximo de la fila actual con el corredor maximo HASTA ESE MOMENTO (de todas las filas anteriores), para 				       actualizar 'maximo' si fuera necesario.
			maximo=maxfila
		i=i+1
	return maximo



def densidad(archivo):
	mapa=open(archivo,'r')
	lista=mapa.readlines()
	paredes=0 #cuenta la cantidad de 1's
	espacios=0 #cuenta la cantidad de 0's
	i=0
	while i<len(lista):
		paredes=paredes+lista[i].count('1')
		espacios=espacios+lista[i].count('0')
		i=i+1
	return paredes/(paredes+espacios)



if (es_mapa(sys.argv[2])):
	s=sys.argv[1]
	if s=='es_mapa':
		print ('Sí, el archivo representa un mapa')
	if s=='cantidad_paredes':
		print ('El mapa tiene ', cantidad_paredes('sys.argv[2]'))
	if s=='espacios_rodeados':
		print ('El mapa tiene ', espacios_rodeados('sys.argv[2]'), ' huecos rodeados')
	if s=='dimensiones':
		print ('El mapa tiene ',(dimensiones('sys.argv[2]'))[0], ' cuadrados de alto y ', (dimensiones('sys.argv[2]'))[1], ' de ancho')
	if s=='corredor_horizontal_mas_largo':
		print ('El corredor horizontal más largo tiene longitud ', corredor_horizontal('sys.argv[2]'))
	if s=='densidad':
		print ('La densidad arquitectónica es de ', densidad('sys.argv[2]'))
else:
	print ('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1')




