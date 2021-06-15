#import.sys

########################### ESTAS SON LAS FUNCIONES DEL TP2 #####################################

# esta funcion lo que hace es, dado un mapa, devuelve la matriz correspondiente al mapa original rodeado por unos
def matriz(nombre):
  mapa = open(nombre,'r')
  matriz = mapa.readlines()
  mapa.close()
  
  # a cada fila le agrego un uno al inicio y al final
  alto = len(matriz)
  i = 0
  matriz_sin_barra_n = []
  while(i < alto-1):
    matriz_sin_barra_n = matriz_sin_barra_n + ['1' + matriz[i].replace('\n','1')]
    i = i + 1
  
  matriz_sin_barra_n = matriz_sin_barra_n  + ['1' + matriz[alto-1] + '1']
  

  # ahora le agrego a la matriz una fila de unos al inicio y al final
  ancho = len(matriz_sin_barra_n[0])

  matriz_rodeada_de_unos = ['1'*ancho] + matriz_sin_barra_n + ['1'*ancho]
  
  
  return matriz_rodeada_de_unos


###################################################################################

# esta funcion decide si es un rectangulo
def es_rectangulo(nombre):

  M = matriz(nombre)

  # cuento la cantidad de filas con la misma longitud que la primera
  altura = len(M)-2 # la cantidad de filas 
  b = 0 #contador
  j = 1
  while j <= altura:
    if len(M[j]) == len(M[0]):
      b = b + 1
    j = j + 1
  
  return altura == b # se fija si la cantidad de filas con la misma longitud que la primera son la altura (o sea, son todas) 



# esta funcion verifica si solo hay ceros y unos (eventualmente \n)
def tiene_solo_ceros_y_unos(nombre):

  mapa=open(nombre,'r')
  x = mapa.read() #guardo en un string todos los caracteres del mapa
  mapa.close()

  #voy contando cada vez que aparece un 0, 1 o \n
  s = len(x) #es la cantidad total de caracteres
  b = 0 #contador
  i = 0
  while i < s:
    if x[i] in ['0', '1', '\n']:
      b = b + 1
    i = i + 1
  
  return s == b #verifica si efectivamente todo lo que conte coincide con la cantidad total de caracteres
  

def es_mapa(nombre):
  a = es_rectangulo(nombre)
  b = tiene_solo_ceros_y_unos(nombre)
  return a and b


#####################################################################3


def dimensiones(archivo):
	M = matriz(archivo) 
	ancho = len(M[0])-2
	alto = len(M)-2
	return [alto, ancho]


#################################################################



def cantidad_paredes(archivo):
	mapa = open(archivo,'r')
	lista = mapa.readlines()
	paredes = 0
	i = 0
	while i< len(lista) :
		contador = lista[i].count('1')
		paredes = paredes + contador
		i = i + 1
	return paredes


##############################################################



def densidad(archivo):
	return cantidad_paredes(archivo)/(dimensiones(archivo)[0]*dimensiones(archivo)[1])



##############################################################


def corredor_horizontal_mas_largo(archivo):
	mapa=open(archivo,'r')
	lista = mapa.readlines()
	maximo=0 #longitud corredor maximo
	i=0
	while i<len(lista): #recorrer las filas del mapa es recorrer cada posicion de la lista (módulo '\n'), así que escribo "FILA" haciendo referencia a "POSICION".
		aux=0 #longitud de un corredor auxiliar en esta fila
		maxfila=0 #longitud del "corredor maximo" de esta fila
		j=0
		while j<len(lista[i]): 
			#cada vez que me paro en un 0, se incrementa la longitud del corredor auxiliar, y la guardo como la longitud maxima de la fila (o sea, 'maxfila'). Esto sucede hasta que, o bien llego a una posicion con un 1 (o al '\n'), o bien termina la fila.
			if lista[i][j]=='0': 
				aux=aux+1
				maxfila=aux
			#si me paro en un caracter distinto de 0, en este caso reinicio 'aux', y actualizo 'maxfila' (para que sea el maximo de esta fila)
			else:
				if maxfila<=aux: 
					maxfila=aux
					aux=0
				else:
					aux=0
			j=j+1
		#el siguiente condicional compara el corredor maximo de la fila actual con el corredor maximo HASTA ESE MOMENTO (de todas las filas anteriores), para actualizar 'maximo' si fuera necesario.
		if maxfila>=maximo:   
			maximo=maxfila
		i=i+1
	return maximo


######################################################################

#Esta funcion devuelve un bool segun la lista tenga todos sus elementos iguales a 1 o no.
def detector_unos(lista):                          
	bool_salida=True        
	indice=0    
	while(indice<len(lista)):
		bool_salida=bool_salida and (lista[indice]=='1')
		indice=indice+1
	return bool_salida


#Función auxiliar:
def cuadrado_de_unos(archivo, nro_fila, indice):
#En list[indice] hay un 0, la funcion recorre "el cuadrado alrededor de este" y se fija que sean todos unos. Devuelve bool. Es decir, recorremos las filas nro_fila-1 y nro_fila+1, y nos fijamos que tengan unos en las posiciones indice-1 indice e indice+1. Y nos fijamos que la fila nro_fila tenga unos en las posiciones indice-1 e indice+1.            
	mapa=open(archivo,'r')
	filas_archivo=mapa.readlines()
	fila_del_cero_con_unos=(filas_archivo[nro_fila][indice-1]=='1') and (filas_archivo[nro_fila][indice+1]=='1')
#La funcion fila_k devuelve una lista de strings, por lo que tengo que buscar '1'.                  
	fila_superior_con_unos=detector_unos(filas_archivo[nro_fila-1][indice-1:indice+2])
#Notar que no hay posibilidad de que nro_fila-1, indice-1<0 porque tuvimos la cautela de separar estos casos en la funcion espacios_rodeados.                                          
	fila_inferior_con_unos=detector_unos(filas_archivo[nro_fila+1][indice-1:indice+2])
	mapa.close()
	return fila_del_cero_con_unos and fila_superior_con_unos and fila_inferior_con_unos

    
def espacios_rodeados(archivo):
#La idea es la siguiente: recorremos las listas del archivo, arrancando de la 2da y hasta la anteultima, y desde la segunda posicion a la anteultima. Cuando detectamos un cero, llamamos la funcion cuadrado_de_unos.
	mapa=open(archivo,'r')
	filas_archivo=mapa.readlines()
	rodeados=0
	nro_fila=1
	#Arranco desde las 2da fila, o sea filas_archivo[1].                                          
	while(nro_fila<len(filas_archivo)-1):
	#Buscamos un 0 encerrado, por lo que arrancamos desde la 2da fila y terminamos en la anteultima.                   
		fila=filas_archivo[nro_fila]                                     
		indice=1
		while(indice<len(fila)-1):
		#Recorremos la fila en busca de un 0 encerrado, por lo que arrancamos desde la segunda posicion hasta la anteultima.                          
			if(fila[indice]=='0' and cuadrado_de_unos(archivo, nro_fila, indice)):
			#Cada vez que detectamos un 0 recorremos "el cuadrado alrededor de él" chequeando que sean todos unos.                     
				rodeados=rodeados+1    
			indice=indice+1
		nro_fila=nro_fila+1
	mapa.close()
	return rodeados











########################## ESTO ES LO NUEVO CORRESPONDIENTE AL TP3 ########################





# las posiciones son listas de pares, la primera coord indica en qué fila estoy, y la segunda, en qué columna
# los indices se mueven como es natural en las matrices (no como acostumbramos en la materia). es decir, van del 1 al ancho o alto, y no, del 0 al ancho-1 y alto-1. esto se debe a que trabajamos con la matriz rodeada por unos definida al principio de todo que nos facilita al momento de definir la funcion de alcanzar con la mano derecha
def pos_valida(nombre, pos):
  if 0 < pos[0] <= dimensiones(nombre)[0] and 0 < pos[1] <= dimensiones(nombre)[1]:
    rv = True
  else:
    rv = False
  
  return rv


##########################################################################



def valor_pos(nombre, pos):
  M = matriz(nombre)
  return M[pos[0]][pos[1]]





################ ALCANZAR CON LA MANO DERECHA ##################################


# Ubicacion de la mano derecha

def mano_derecha_al_este(matriz, pos):
  mano_derecha = [pos[0], pos[1]+1]
  return [pos, mano_derecha]


def mano_derecha_al_oeste(matriz, pos):
  mano_derecha = [pos[0], pos[1]-1]
  return [pos, mano_derecha]

def mano_derecha_al_norte(matriz, pos):
  mano_derecha = [pos[0]-1, pos[1]]
  return [pos, mano_derecha]


def mano_derecha_al_sur(matriz, pos):
  mano_derecha = [pos[0]+1, pos[1]]
  return [pos, mano_derecha]


def mano_derecha_al_noreste(matriz, pos):
  mano_derecha = [pos[0]-1, pos[1]+1]
  return [pos, mano_derecha]


def mano_derecha_al_suroeste(matriz, pos):
  mano_derecha = [pos[0]+1, pos[1]-1]
  return [pos, mano_derecha]

def mano_derecha_al_noroeste(matriz, pos):
  mano_derecha = [pos[0]-1, pos[1]-1]
  return [pos, mano_derecha]


def mano_derecha_al_sureste(matriz, pos):
  mano_derecha = [pos[0]+1, pos[1]+1]
  return [pos, mano_derecha]







# La siguientes funciones indican hacia donde se mueve el explorador dependiendo de su posicion y la ubicacion de su mano derecha


# **** 
# *01*
def si_pared_al_este(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos-1][columna_de_pos] == '0' and matriz[fila_de_mano_der-1][columna_de_mano_der] == '1':
    # *01*    si esta es la situación
    # *01*
    pos_nueva = [fila_de_pos-1, columna_de_pos]
    mano_der_nueva = [fila_de_mano_der-1, columna_de_mano_der]
    # *01*    me muevo hacia arriba
    # ****

  elif matriz[fila_de_pos-1][columna_de_pos] == '0' and matriz[fila_de_mano_der-1][columna_de_mano_der] == '0':
    # *00*    si esta es la situación
    # *01*
    pos_nueva = [fila_de_pos-1, columna_de_pos]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der]
    # *0**    comienzo a girar hacia el este
    # **1*

  elif matriz[fila_de_pos-1][columna_de_pos] == '1':
    # *1**    si esta es la situación
    # *01*
    pos_nueva = [fila_de_pos, columna_de_pos]
    mano_der_nueva = [fila_de_pos-1, columna_de_pos]
    # *1**    solo muevo mi mano a la pared de arriba y sigo parado en el mismo lugar
    # *0**


  return [pos_nueva, mano_der_nueva]




# *10*
# ****
def si_pared_al_oeste(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos+1][columna_de_pos] == '0' and matriz[fila_de_mano_der+1][columna_de_mano_der] == '1':
    # *10*
    # *10*
    pos_nueva = [fila_de_pos+1, columna_de_pos]
    mano_der_nueva = [fila_de_mano_der+1, columna_de_mano_der]
    # ****
    # *10*

  elif matriz[fila_de_pos+1][columna_de_pos] == '0' and matriz[fila_de_mano_der+1][columna_de_mano_der] == '0':
    # *10*
    # *00*
    pos_nueva = [fila_de_pos+1, columna_de_pos]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der]
    # *1**
    # **0*

  elif matriz[fila_de_pos+1][columna_de_pos] == '1':
    # *10*
    # **1*
    pos_nueva = [fila_de_pos, columna_de_pos]
    mano_der_nueva = [fila_de_pos+1, columna_de_pos]
    # **0*
    # **1*

  return [pos_nueva, mano_der_nueva]





# **1*
# **0*
def si_pared_al_norte(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos][columna_de_pos-1] == '0' and matriz[fila_de_mano_der][columna_de_mano_der-1] == '1':
    # *11*
    # *00*
    pos_nueva = [fila_de_pos, columna_de_pos-1]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der-1]
    # *1**
    # *0**

  elif matriz[fila_de_pos][columna_de_pos-1] == '0' and matriz[fila_de_mano_der][columna_de_mano_der-1] == '0':
    # *01*
    # *00*
    pos_nueva = [fila_de_pos, columna_de_pos-1]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der]
    # **1*
    # *0**

  elif matriz[fila_de_pos][columna_de_pos-1] == '1':
    # **1*
    # *10*
    pos_nueva = [fila_de_pos, columna_de_pos]
    mano_der_nueva = [fila_de_pos, columna_de_pos-1]
    # ****
    # *10*

  return [pos_nueva, mano_der_nueva]




# *0**
# *1**
def si_pared_al_sur(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos][columna_de_pos+1] == '0' and matriz[fila_de_mano_der][columna_de_mano_der+1] == '1':
    # *00*
    # *11* 
    pos_nueva = [fila_de_pos, columna_de_pos+1]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der+1]
    # **0*
    # **1*

  elif matriz[fila_de_pos][columna_de_pos+1] == '0' and matriz[fila_de_mano_der][columna_de_mano_der+1] == '0':
    # *00*
    # *10* 
    pos_nueva = [fila_de_pos, columna_de_pos+1]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der]
    # **0*
    # *1** 

  elif matriz[fila_de_pos][columna_de_pos+1] == '1':
    # *01*
    # *1**
    pos_nueva = [fila_de_pos, columna_de_pos]
    mano_der_nueva = [fila_de_pos, columna_de_pos+1]
    # *01*
    # ****

  return [pos_nueva, mano_der_nueva]



# estos son los casos en los que estoy girando hacia un lado


# **1*
# *0**
def si_pared_al_noreste(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos-1][columna_de_pos] == '0':
    # *01*    si esta es la situación
    # *0**
    pos_nueva = [fila_de_pos-1, columna_de_pos]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der]
    # *01*    termino de girar hacia el norte
    # ****
  
  return [pos_nueva, mano_der_nueva]




# **0*
# *1**
def si_pared_al_suroeste(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos+1][columna_de_pos] == '0':
    # **0*    
    # *10*
    pos_nueva = [fila_de_pos+1, columna_de_pos]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der]
    # ****   
    # *10*
  
  return [pos_nueva, mano_der_nueva]


# *1**
# **0*
def si_pared_al_noroeste(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos][columna_de_pos-1] == '0':
    # *1**    
    # *00*
    pos_nueva = [fila_de_pos, columna_de_pos-1]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der] 
    # *1**   
    # *0**
  
  return [pos_nueva, mano_der_nueva]


# *0**
# **1*
def si_pared_al_sureste(matriz, pos_y_mano_der):

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  if matriz[fila_de_pos][columna_de_pos+1] == '0':
    # *00*    
    # **1*
    pos_nueva = [fila_de_pos, columna_de_pos+1]
    mano_der_nueva = [fila_de_mano_der, columna_de_mano_der]
    # **0*   
    # **1*
  
  return [pos_nueva, mano_der_nueva]







#se fija si un lugar es un cruce entre dos es_cruce_de_pasillos

# 101
# 000
# 101

#PRE: el valor de la matriz en pos es 0
def es_cruce_de_pasillos(matriz, pos):
  if matriz[pos[0]+1][pos[1]] == '0' and matriz[pos[0]-1][pos[1]] == '0' and matriz[pos[0]][pos[1]+1] == '0' and matriz[pos[0]][pos[1]-1] == '0':
    rv = True
  else:
    rv = False
  
  return rv






# la siguiente función resuelve el problema de: dado un mapa, una posición inicial (junto con su mano derecha) y una posición de destino, decidir si se puede llegar desde una hacia otra con el metodo de la mano derecha

# PRE: pos_y_mano_der es una lista cuya primer coord es una ubicación en el mapa que está vacía, y su segunda, es una posición adyacente a la primera, donde se encuentra una pared. Y además, pos_destino es una lista que corresponde a un lugar vacío del mapa que a su alrededor tiene por lo menos una pared.

def alcanzar_con_mano_derecha(matriz, pos_y_mano_der, pos_destino):

  pos_inicial = pos_y_mano_der #guardo la posicion inicial teniendo en cuenta tanto dónde estoy parado y en dónde está apoyada mi mano derecha

  # primero me muevo una vez para ver si llego

  fila_de_pos = pos_y_mano_der[0][0]
  columna_de_pos = pos_y_mano_der[0][1]
  fila_de_mano_der = pos_y_mano_der[1][0]
  columna_de_mano_der = pos_y_mano_der[1][1]

  # me fijo todas las posibilidades dependiendo de dónde está ubicada la mano derecha

  if fila_de_pos == fila_de_mano_der and columna_de_pos+1 == columna_de_mano_der: # si la mano derecha está al este
      pos_y_mano_der = si_pared_al_este(matriz, pos_y_mano_der)
    
  elif fila_de_pos == fila_de_mano_der and columna_de_pos-1 == columna_de_mano_der: # si la mano derecha está al oeste
      pos_y_mano_der = si_pared_al_oeste(matriz, pos_y_mano_der)

  elif columna_de_pos == columna_de_mano_der and fila_de_pos-1 == fila_de_mano_der: # si la mano derecha está al norte
      pos_y_mano_der = si_pared_al_norte(matriz, pos_y_mano_der)
    
  elif columna_de_pos == columna_de_mano_der and fila_de_pos+1 == fila_de_mano_der: # si la mano derecha está al sur
      pos_y_mano_der = si_pared_al_sur(matriz, pos_y_mano_der)

  elif columna_de_pos+1 == columna_de_mano_der and fila_de_pos-1 == fila_de_mano_der: # si la mano derecha está al noreste
      pos_y_mano_der = si_pared_al_noreste(matriz, pos_y_mano_der)
  
  elif columna_de_pos-1 == columna_de_mano_der and fila_de_pos+1 == fila_de_mano_der: # si la mano derecha está al suroeste
      pos_y_mano_der = si_pared_al_suroeste(matriz, pos_y_mano_der)
  
  elif columna_de_pos-1 == columna_de_mano_der and fila_de_pos-1 == fila_de_mano_der: # si la mano derecha está al noroeste
      pos_y_mano_der = si_pared_al_noroeste(matriz, pos_y_mano_der)

  elif columna_de_pos+1 == columna_de_mano_der and fila_de_pos+1 == fila_de_mano_der: # si la mano derecha está al sureste
      pos_y_mano_der = si_pared_al_sureste(matriz, pos_y_mano_der)

  # ahora me sigo moviendo hasta que llegue a la posicion de destino o hasta que vuelva a mi posicion incial (considerando no solo dónde comencé parado, sino también, dónde apoyé mi mano derecha). esto es en el caso en que no haya un camino que conecte las posiciones

  while(not (pos_y_mano_der == pos_inicial or pos_y_mano_der[0] == pos_destino)):
    
    # con el siguiente print se puede ver el recorrido del explorador:
    print(pos_y_mano_der) 

    fila_de_pos = pos_y_mano_der[0][0]
    columna_de_pos = pos_y_mano_der[0][1]
    fila_de_mano_der = pos_y_mano_der[1][0]
    columna_de_mano_der = pos_y_mano_der[1][1]

    if fila_de_pos == fila_de_mano_der and columna_de_pos+1 == columna_de_mano_der:
      pos_y_mano_der = si_pared_al_este(matriz, pos_y_mano_der)
    
    elif fila_de_pos == fila_de_mano_der and columna_de_pos-1 == columna_de_mano_der:
      pos_y_mano_der = si_pared_al_oeste(matriz, pos_y_mano_der)
    
    elif columna_de_pos == columna_de_mano_der and fila_de_pos-1 == fila_de_mano_der:
      pos_y_mano_der = si_pared_al_norte(matriz, pos_y_mano_der)

    elif columna_de_pos == columna_de_mano_der and fila_de_pos+1 == fila_de_mano_der:
      pos_y_mano_der = si_pared_al_sur(matriz, pos_y_mano_der)

    elif columna_de_pos+1 == columna_de_mano_der and fila_de_pos-1 == fila_de_mano_der: 
      pos_y_mano_der = si_pared_al_noreste(matriz, pos_y_mano_der)
  
    elif columna_de_pos-1 == columna_de_mano_der and fila_de_pos+1 == fila_de_mano_der: 
      pos_y_mano_der = si_pared_al_suroeste(matriz, pos_y_mano_der)
  
    elif columna_de_pos-1 == columna_de_mano_der and fila_de_pos-1 == fila_de_mano_der: 
      pos_y_mano_der = si_pared_al_noroeste(matriz, pos_y_mano_der)

    elif columna_de_pos+1 == columna_de_mano_der and fila_de_pos+1 == fila_de_mano_der: 
      pos_y_mano_der = si_pared_al_sureste(matriz, pos_y_mano_der)
  

  # por último distingo entre las dos posibilidades: si llegué a destino, devuelvo True, y si en cambio volví a la posición original, devuelvo False 
  if pos_y_mano_der == pos_inicial:
    pude_llegar = False
  else:
    pude_llegar = True


  return pude_llegar




############################ IMPLEMENTACION TAD MAPA ###################################


class Mapa:

  def __init__(self, nombre_archivo):    
    self.nombre = nombre_archivo   

  def alto(self):
    return dimensiones(self.nombre)[0]
  
  def ancho(self):
    return dimensiones(self.nombre)[1]

  def posicion(self, pos):
    return valor_pos(self.nombre, pos)

  def es_posicion_valida(self, pos):
    return pos_valida(self.nombre, pos)

  def cantidad_paredes(self):
    return cantidad_paredes(self.nombre)

  def corredor_horizontal_mas_largo(self):
    return corredor_horizontal_mas_largo(self.nombre)

  def densidad_arquitectonica(self):
    return densidad(self.nombre)
  

  #PRE: tanto pos inicial como destino son lugares vacíos (porque sino, dependería de qué lado uno quiera llegar si fuese una pared)

  def alcanzar_con_mano_derecha(self, pos_inicial, pos_destino):

    Matriz = matriz(self.nombre)
    fila_pos_inicial = pos_inicial[0]
    columna_pos_inicial = pos_inicial[1]

    if Matriz[fila_pos_inicial][columna_pos_inicial+1] == '1':
      pude_llegar_con_mano_al_este = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_este(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_este)
    else:
      pude_llegar_con_mano_al_este = False
    
    if Matriz[fila_pos_inicial][columna_pos_inicial-1] == '1':
      pude_llegar_con_mano_al_oeste = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_oeste(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_oeste)
    else:
      pude_llegar_con_mano_al_oeste = False

    if Matriz[fila_pos_inicial-1][columna_pos_inicial] == '1':
      pude_llegar_con_mano_al_norte = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_norte(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_norte)
    else:
      pude_llegar_con_mano_al_norte = False
    
    if Matriz[fila_pos_inicial+1][columna_pos_inicial] == '1':
      pude_llegar_con_mano_al_sur = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_sur(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_sur)
    else:
      pude_llegar_con_mano_al_sur = False
    
    if Matriz[fila_pos_inicial-1][columna_pos_inicial+1] == '1' and es_cruce_de_pasillos(Matriz, pos_inicial):
      pude_llegar_con_mano_al_noreste = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_noreste(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_noreste)
    else:
      pude_llegar_con_mano_al_noreste = False
    
    if Matriz[fila_pos_inicial+1][columna_pos_inicial-1] == '1' and es_cruce_de_pasillos(Matriz, pos_inicial):
      pude_llegar_con_mano_al_suroeste = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_suroeste(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_suroeste)
    else:
      pude_llegar_con_mano_al_suroeste = False
    
    if Matriz[fila_pos_inicial-1][columna_pos_inicial-1] == '1' and es_cruce_de_pasillos(Matriz, pos_inicial):
      pude_llegar_con_mano_al_noroeste = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_noroeste(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_noroeste)
    else:
      pude_llegar_con_mano_al_noroeste = False
    
    if Matriz[fila_pos_inicial+1][columna_pos_inicial+1] == '1' and es_cruce_de_pasillos(Matriz, pos_inicial):
      pude_llegar_con_mano_al_sureste = alcanzar_con_mano_derecha(Matriz, mano_derecha_al_sureste(Matriz, pos_inicial), pos_destino)
      print(pude_llegar_con_mano_al_sureste)
    else:
      pude_llegar_con_mano_al_sureste = False
    


    pude_llegar = pude_llegar_con_mano_al_este or pude_llegar_con_mano_al_norte or pude_llegar_con_mano_al_oeste or pude_llegar_con_mano_al_sur or pude_llegar_con_mano_al_noreste or pude_llegar_con_mano_al_noroeste or pude_llegar_con_mano_al_suroeste or pude_llegar_con_mano_al_sureste


    return pude_llegar



m = Mapa('otro.txt')
print(m.alcanzar_con_mano_derecha([5,7],[1,1]))