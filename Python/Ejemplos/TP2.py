import sys
###########################################################################################################################
#ACLARACION: Consideramos como un buen mapa el dado en la carpeta de Ejemplos. Es decir, asumimos que un buen mapa no posee filas vacias. En particular, no debe poseer lineas con '\n' como primer (y unico) elemento.

###########################################################################################################################
#Esta seccion corresponde a la funcion es_mapa:       

def quitar_barra_n(lista):
#Esto es porque cada salto de renglon se lee como \n al final de la linea, y eso no lo queremos en la lista, asi que lo borramos. (Lo borramos de las listas que lo tienen, porque list.remove nos devuelve error si no hay nada)                              
    if('\n' in lista):                      
        lista.remove('\n')
    return lista

def es_rectangulo(file):
#Devuelve un bool segun el archivo sea un rectangulo o no.                                                        
    archivo=open(file,'r')
    filas_archivo=archivo.readlines()
    longitud=len(quitar_barra_n(list(filas_archivo[0])))
#Le saco \n a la primera fila del archivo, pero como file.readlines[0] lo lee como un solo string, primero tengo que convertirlo a una lista de strings.                        
    i=0
    bool_final=True
    while(i<len(filas_archivo)):
#Esta secuencia hace las veces del for line in file (la uso varias veces durante el programa).                                                
        if(len(quitar_barra_n(list(filas_archivo[i])))!=longitud):
            bool_final=bool_final and False
        i=i+1
    #archivo.close()
    return bool_final


def unos_y_ceros(file):
#Aca nos fijamos que los caracteres de las filas del archivo sean 0 o 1.                                                         
    archivo=open(file,'r')
    bool_salida=True
    filas_archivo=archivo.readlines()
    i=0
    bool_salida=True
    while(i<len(filas_archivo)):
                indice=0
                fila=quitar_barra_n(list(filas_archivo[i]))
                while(indice<len(fila)):
                        if(fila[indice]!='0' and fila[indice]!='1'):#Si la fila tiene algo distinto de 0 o 1, bool_salida=False.
                                bool_salida=bool_salida and False
                        indice=indice+1
                i=i+1
    archivo.close()
#Esto es por seguridad para que no se dañe el archivo si permanece abierto.
    return bool_salida

def es_mapa(file):
    return es_rectangulo(file) and unos_y_ceros(file)

###########################################################################################################################
#Esta seccion corresponde a la funcion cantidad_paredes: (puede usar funciones anteriores)

def cantidad_paredes(file):
    archivo=open(file,'r')
    contador=0
    filas_archivo=archivo.readlines()
    i=0
    while(i<len(filas_archivo)):
        indice=0
        fila=quitar_barra_n(list(filas_archivo[i]))
        while(indice<len(fila)):
#Recorro todos los elementos de la fila i-ésima, contando cada 1 que tenga.                                
                if(fila[indice]=='1'):
                        contador=contador+1
                indice=indice+1
        i=i+1
    archivo.close()
    return contador

###########################################################################################################################
#Esta seccion corresponde a la funcion espacios_rodeados: (puede usar funciones anteriores)

def detector_unos(lista):
#Esta funcion devuelve un bool segun la lista tenga todos sus elementos iguales a 1 o no.                               
    bool_salida=True        
    indice=0    
    while(indice<len(lista)):
        bool_salida=bool_salida and (lista[indice]=='1')
        indice=indice+1
    return bool_salida

def cuadrado_de_unos(file, nro_fila, indice):
#En list[indice] hay un 0, la funcion recorre "el cuadrado alrededor de este" y se fija que sean todos unos. Devuelve bool. Es decir, recorremos las filas nro_fila-1 y nro_fila+1, y nos fijamos que tengan unos en las posiciones indice-1 indice e indice+1. Y nos fijamos que la fila nro_fila tenga unos en las posiciones indice-1 e indice+1.            
    archivo=open(file,'r')
    filas_archivo=archivo.readlines()
    fila_del_cero_con_unos=(filas_archivo[nro_fila][indice-1]=='1') and (filas_archivo[nro_fila][indice+1]=='1')
#La funcion fila_k devuelve una lista de strings, por lo que tengo que buscar '1'.                  
    fila_superior_con_unos=detector_unos(filas_archivo[nro_fila-1][indice-1:indice+2])
#Notar que no hay posibilidad de que nro_fila-1, indice-1<0 porque tuvimos la cautela de separar estos casos en la funcion espacios_rodeados.                                          
    fila_inferior_con_unos=detector_unos(filas_archivo[nro_fila+1][indice-1:indice+2])
    archivo.close()
    return fila_del_cero_con_unos and fila_superior_con_unos and fila_inferior_con_unos
    
def espacios_rodeados(file):
#La idea es la siguiente: recorremos las listas del archivo, arrancando de la 2da y hasta la anteultima, y desde la segunda posicion a la anteultima. Cuando detecttamos un cero, llamamos la funcion cuadrado_de_unos.
    archivo=open(file,'r')
    filas_archivo=archivo.readlines()
    rodeados=0
    nro_fila=1
#Arranco desde las 2da fila, o sea filas_archivo[1].                                          
    while(nro_fila<len(filas_archivo)-1):
#Buscamos un 0 encerrado, por lo que arrancamos desde la 2da fila y terminamos en la anteultima.                   
        fila=filas_archivo[nro_fila]                                     
        indice=1
        while(indice<len(fila)-1):
#Recorremos la fila en busca de un 0 encerrado, por lo que arrancamos desde la segunda posicion hasta la anteultima.                          
                if(fila[indice]=='0' and cuadrado_de_unos(file, nro_fila, indice)):
#Cada vez que detectamos un 0 recorremos "el cuadrado alrededor de él" chequeando que sean todos unos.                     
                        rodeados=rodeados+1    
                indice=indice+1
        nro_fila=nro_fila+1
    archivo.close()
    return rodeados

###########################################################################################################################
#Esta seccion corresponde a la funcion dimensiones: (puede usar funciones anteriores)

def dimensiones(file):                                          
    archivo=open(file,'r')
    filas_archivo=archivo.readlines()
    dim=[len(filas_archivo),len(quitar_barra_n(list(filas_archivo[0])))]
#Como solo tiene sentido hablar de columnas para un buen mapa, la cantidad de columnas es la cantidad de elementos de cualquiera de sus filas.                    
    archivo.close()
    return dim

###########################################################################################################################
#Esta seccion corresponde a la funcion corredor_horizontal_mas_largo: (puede usar funciones anteriores)

def detector_ceros(lista):
#Esta funcion devuelve un bool segun la lista tenga todos sus elementos iguales a 0 o no.                               
    bool_salida=True        
    indice=0    
    while(indice<len(lista)):
        bool_salida=bool_salida and (lista[indice]=='0')
        indice=indice+1
    return bool_salida

def lista_posiciones_unos(line):
#Dada una lista de ceros y unos, devuelve una lista con las posiciones de los unos en la lista de entrada.                          
    indice=0
    lista_unos=[]
    while(indice<len(line)):
        if(line[indice]=='1'):
            lista_unos.append(indice)
        indice=indice+1
    return lista_unos

def diferencias_posiciones_unos(line):
#Una forma de calcular un corredor es restar las posiciones de los unos que encierran los corredores.                    
    indice=0
    diferencias=[]
    lista_unos=lista_posiciones_unos(line)
    diferencias.append(lista_unos[0])
#Agrego la primera posicion de lista_unos, porque esa ya me indica cuantos ceros hay antes que ese uno.                                               
    diferencias.append(len(line)-1-lista_unos[len(lista_unos)-1])
#Agrego la diferencia entre el largo de la fila y la ultima posicion de lista_unos.                   
    while(indice<len(lista_unos)-1):
#Agrego las diferencias de posiciones consecutivas de la lista_unos (salvo el caso de la ultima posicion).                                                
        diferencias.append(lista_unos[indice+1]-lista_unos[indice]-1)
        indice=indice+1
    return diferencias

def maxima_secuencia_ceros(line):
#La maxima secuencia de ceros es simplemente el maximo de la lista de las diferencias de los unos que a encierran los ceros.                               
    return max(diferencias_posiciones_unos(line))

def corredor_horizontal_mas_largo(file):
#Recorremos todas las filas del archivo calculando el corredor mas largo de la forma explicada en la funcion diferencias_posiciones_unos.                        
    archivo=open(file,'r')
    corredores=[]
    filas_archivo=archivo.readlines()
    i=0
    while(i<len(filas_archivo)):
        fila=quitar_barra_n(list(filas_archivo[i]))
        if(detector_ceros(fila)==1):
                corredores.append(len(fila))
        else:
                corredores.append(maxima_secuencia_ceros(fila))
        i=i+1
    archivo.close()
    return max(corredores)
#Devolvemos el corredor mas largo.                                  

###########################################################################################################################
#Esta seccion corresponde a la funcion densidad: (puede usar funciones anteriores)

def densidad(file):
    return cantidad_paredes(file)/(dimensiones(file)[0]*dimensiones(file)[1])

###########################################################################################################################
#Esta seccion corresponde a la comunicacion con el usuario:
if(es_mapa(sys.argv[2])==True):
    if (sys.argv[1]=='es_mapa' or sys.argv[1]=='cantidad_paredes' or sys.argv[1]=='espacios_rodeados' or sys.argv[1]=='dimensiones' or sys.argv[1]=='corredor_horizontal_mas_largo' or sys.argv[1]=='densidad'):
        if (sys.argv[1]=='es_mapa'):
            print('Sí, el archivo representa un mapa.')
        if(sys.argv[1]=='cantidad_paredes'):
            print('El mapa tiene ' + str(cantidad_paredes(sys.argv[2])) + ' paredes.')
        if(sys.argv[1]=='espacios_rodeados'):
            print('El mapa tiene ' + str(espacios_rodeados(sys.argv[2])) + ' huecos rodeados de paredes.')
        if(sys.argv[1]=='dimensiones'):
            print('El mapa tiene ' + str(dimensiones(sys.argv[2])[1]) + ' cuadrados de ancho y ' + str(dimensiones(sys.argv[2])[0]) + ' de alto.')
        if(sys.argv[1]=='corredor_horizontal_mas_largo'):
            print('El corredor horizontal más largo tiene longitud ' + str(corredor_horizontal_mas_largo(sys.argv[2])) + '.')
        if(sys.argv[1]=='densidad'):
            print('La densidad arquitectónica es de ' + str(densidad(sys.argv[2])) + '.')
    else:
        print('La función ingresada no es correcta.')
else:
    print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')
