import sys
entrada_1=input('Ingrese el nombre de la funcion que desea ejecutar: ')
entrada_2=input('Ingrese el nombre del archivo (no es necesario aclarar su formato): ')
if(entrada_2[len(entrada_2)-1-4:len(entrada_2)]=='.txt'):               #Esto es para no preocuparse de aclarar el formato del archivo.
        True
else:
        entrada_2=entrada_2+'.txt'
if(' ' in entrada_1):                                                   #Esto es para no preocuparse de poner guiones bajos en vez de espacios cuando llamamos a las funciones.(NO PONER MAS ESPACIOS QUE LOS ESTRICTAMENTE NECESARIOS)
        entrada_1=entrada_1.replace(' ','_')

#Comentario previo: vamos a ver repetida varias veces la secuencia:
        
##        last_pos = 0
##        while(file.readline()!=''):                       #Esto recorre todas las filas del archivo.
##            file.seek(last_pos)                           #Aca llevamos el puntero a la posicion last_pos del archivo.
##            linea=file.readline()
        
##            '''''''algoritmo'''''''
        
##            last_pos=file.tell()                          #Cuando termine la iteracion del ciclo, last_pos tiene que ser la posicion actual del puntero.
##
##Esto es porque reemplaza el for linea in file.        
###########################################################################################################################
#Esta seccion corresponde a la funcion es_mapa:

        

def quitar_barra_n(lista):                              #Esto es porque cada salto de renglon se lee como \n al final de la linea, y eso no lo queremos en la lista, asi que lo borramos. (De las listas que lo tienen, porque list.remove nos tira error si no hay nada)
        if('\n' in lista):                      
                lista.remove('\n')
        return lista

def vector_columnas(file):                              #Devuelve un vector con la cantidad de columnas de cada fila.
        file=open(entrada_2,'r')                        #En cada funcion que use el archivo, lo vuelvo a abrir para resetear el puntero.
        columnas=[]
        #for linea in file
        last_pos = 0
        while(file.readline()!=''):                     #La idea es la siguiente: recorremos cada linea del archivo y contamos cuantos elementos tiene luego de transformarla en una lista (ie, la cantidad de columnas).
            file.seek(last_pos)
            linea=file.readline()

            #while(linea.startswith('\n')==True):        #Esto es para omitir las primeras filas vacias del archivo, si es que hay alguna.
            #        linea=file.readline()
            #        if(list(linea).startswith
            #        last_pos=file.tell()
            fila=quitar_barra_n(list(linea))            #Convierto la linea en lista de strings y le saco el \n del final.
            #if(fila==[]):                               #Aca analizamos si la fila actual es vacia, y agregamos un -1 a columnas para que elementos_repetidos nos de False.
            #        file.seek(last_pos-columnas[len(columnas)-1)
            columnas.append(len(fila))                  #Guardo en la variable auxiliar 'tamaños' la cantidad de elementos de cada linea del archivo (ie, la cantidad de columnas de cada fila)
            last_pos=file.tell()
        
        file.close()                                    #Siempre que en una funcion abra un archivo, al final de la misma lo cierro por cuestiones seguridad ante posibles daños al archivo.
        return columnas

def cantidad_filas(file):                               #Notar que ignoramos lineas vacias y comentarios.
        file=open(entrada_2,'r')
        cantidad=0
        #for linea in file
        last_pos = 0
        while(file.readline()!=''):                     
            file.seek(last_pos)                         
            linea=file.readline()
            
            if((linea.lstrip('\t')).startswith('\n')==False and (linea.lstrip('\t')).startswith('#')==False):               #Aca descartamos las lineas que arrancan con \n y con # (ie, lineas vacias o comentarios)
                        cantidad=cantidad+1
                        
            last_pos=file.tell()                        
        file.close()
        return cantidad
    
def elementos_repetidos(lista):                                                 #Esta funcion devuelve un bool segun la lista tenga todos sus elementos iguales o no.
        indice=0
        bool_final=True
        while(indice<len(lista)-1):                                             #Aca nos fijamos que todas las lineas de file tengan la misma cantidad de columnas (ie, que sea un rectangulo)
                bool_aux=bool_final
                bool_final=bool_aux and (lista[indice]==lista[indice+1])
                indice=indice+1
        return bool_final

def unos_y_ceros(file):                                                         #Aca nos fijamos que los caracteres de las filas del archivo sean 0 o 1
        file=open(entrada_2,'r')
        bool_salida=True
        #for linea in file
        last_pos = 0
        while(file.readline()!=''):                     
            file.seek(last_pos)                         
            linea=file.readline()

            indice=0
            fila=quitar_barra_n(list(linea))
            while(indice<len(fila)):
                if(fila[indice]!='0' and fila[indice]!='1'):                    #Si la fila tiene algo distinto de 0 o 1, bool_salida=False.
                    bool_salida=bool_salida and False
                indice=indice+1
            
            last_pos=file.tell()
        file.close()
        return bool_salida

def es_mapa(file):
        file=open(entrada_2,'r')
        columnas=vector_columnas(file)
        es_rectangulo=elementos_repetidos(columnas)                     #Chequeamos que sea un rectangulo, controlando que todas las posiciones de la lista con la cantidad de columnas de cada fila coincidan.
        unos_ceros=unos_y_ceros(file)                                   #Chequeamos que contenga solo unos y ceros
        file.close()
        return es_rectangulo and unos_ceros

###########################################################################################################################
#Esta seccion corresponde a la funcion cantidad_paredes: (puede usar funciones anteriores)

def cantidad_paredes(file):
        file=open(entrada_2,'r')
        contador=0
        #for linea in file
        last_pos = 0
        while(file.readline()!=''):                     
            file.seek(last_pos)                         
            linea=file.readline()

            indice=0
            fila=quitar_barra_n(list(linea))
            while(indice<len(fila)):
                if(fila[indice]=='1'):
                    contador=contador+1
                indice=indice+1
            
            last_pos=file.tell()
        file.close()
        return contador

###########################################################################################################################
#Esta seccion corresponde a la funcion espacios_rodeados: (puede usar funciones anteriores)

def fila_k(file,k):                                     #Devuelve la fila k del archivo en forma de lista.
        file=open(entrada_2,'r')
        contador=1
        while(contador<=k):                             #Y lo que hacemos para lograrlo es leer el archivo k veces.
                fila=file.readline()
                contador=contador+1
        file.close()
        return fila
        
def detector_unos(lista):                               #Esta funcion devuelve un bool segun la lista tenga todos sus elementos iguales a 1 o no.
        bool_salida=True        
        indice=0    
        while(indice<len(lista)):
                bool_salida=bool_salida and (lista[indice]=='1')
                indice=indice+1
        return bool_salida

def cuadrado_de_unos(file, nro_fila, index):            #En list[index] hay un 0, la funcion recorre "el cuadrado alrededor de este" y se fija que sean todos unos. Devuelve bool. Es decir, recorremos las filas nro_fila-1 y nro_fila+1, y nos fijamos que tengan unos en las posiciones index-1 index e index+1. Y nos fijamos que la fila nro_fila tenga unos en las posiciones index-1 e index+1.
        file=open(entrada_2,'r')
        fila_del_cero_con_unos=(fila_k(file,nro_fila)[index-1]=='1') and (fila_k(file,nro_fila)[index+1]=='1')                  #La funcion fila_k devuelve una lista de strings, por lo que tengo que buscar '1'.
        fila_superior_con_unos=detector_unos(fila_k(file,nro_fila+1)[index-1:index+2])                                          #Notar que no hay posibilidad de que nro_fila-1, index-1<0 porque tuvimos la cautela de separar estos casos en la funcion espacios_rodeados.
        fila_inferior_con_unos=detector_unos(fila_k(file,nro_fila-1)[index-1:index+2])
        file.close()
        return fila_del_cero_con_unos and fila_superior_con_unos and fila_inferior_con_unos
    
def espacios_rodeados(file):                                    #La idea es la siguiente: recorremos las listas del archivo, arrancando de la 2da y hasta la anteultima, y desde la segunda posicion a la ultima. Cuando detecttamos un 0, llamamos la funcion cuadrado_de_unos.
        file=open(entrada_2,'r')
        rodeados=0
        nro_fila=2
        while(nro_fila<cantidad_filas(file)):                   #Buscamos un 0 encerrado, por lo que arrancamos desde la 2da fila y terminamos en la anteultima.
            fila=fila_k(file,nro_fila)                                     
            indice=1
            while(indice<len(fila)-1):                          #Recorremos la fila en busca de un 0 encerrado, por lo que arrancamos desde la segunda posicion hasta la anteultima.
                if(fila[indice]=='0' and cuadrado_de_unos(file, nro_fila, indice)):                     #Cada vez que detectamos un 0 recorremos "el cuadrado alrededor de él" chequeando que sean todos unos
                    rodeados=rodeados+1    
                indice=indice+1
            nro_fila=nro_fila+1
        file.close()
        return rodeados

###########################################################################################################################
#Esta seccion corresponde a la funcion dimensiones: (puede usar funciones anteriores)

def dimensiones(file):                                          #Devuelve dim=[#filas,#columnas].
        file=open(entrada_2,'r')
        fila=quitar_barra_n(list(file.readline()))
        dim=[cantidad_filas(file),len(fila)]                    #Como solo tiene sentido hablar de columnas para un buen mapa, la cantidad de columnas es la cantidad de elementos de cualquiera de sus lineas
        file.close()
        return dim

###########################################################################################################################
#Esta seccion corresponde a la funcion corredor_horizontal_mas_largo: (puede usar funciones anteriores)

def detector_ceros(lista):                               #Esta funcion devuelve un bool segun la lista tenga todos sus elementos iguales a 0 o no.
        bool_salida=True        
        indice=0    
        while(indice<len(lista)):
                bool_salida=bool_salida and (lista[indice]=='0')
                indice=indice+1
        return bool_salida

def lista_posiciones_unos(line):                          #Dada una lista de ceros y unos, devuelve una lista con las posiciones de los unos en la lista de entrada.
        indice=0
        lista_unos=[]
        while(indice<len(line)):
                if(line[indice]=='1'):
                        lista_unos.append(indice)
                indice=indice+1
        return lista_unos

def diferencias_posiciones_unos(line):                    #Una forma de calcular un corredor es restar las posiciones de los unos que encierran los corredores.
        indice=0
        diferencias=[]
        lista_unos=lista_posiciones_unos(line)
        diferencias.append(lista_unos[0])                                               #Agrego la primera posicion de lista_unos, porque esa ya me indica cuantos ceros hay antes que ese uno.
        diferencias.append(len(line)-1-lista_unos[len(lista_unos)-1])                   #Agrego la diferencia entre el largo de la fila y la ultima posicion de lista_unos.
        while(indice<len(lista_unos)-1):                                                #Agrego las diferencias de posiciones consecutivas de la lista_unos (salvo el caso de la ultima posicion).
                diferencias.append(lista_unos[indice+1]-lista_unos[indice]-1)
                indice=indice+1
        return diferencias

def maxima_secuencia_ceros(line):                               #La maxima secuencia de ceros es simplemente el maximo de la lista de las diferencias de los unos que a encierran los ceros.
        return max(diferencias_posiciones_unos(line))

def corredor_horizontal_mas_largo(file):                        #Recorremos todas las filas del archivo calculando el corredor mas largo de la forma explicada en la funcion diferencias_posiciones_unos.
        file=open(entrada_2,'r')
        corredores=[]
        #for linea in file
        last_pos = 0
        while(file.readline()!=''):                     
            file.seek(last_pos)                         
            linea=file.readline()

            fila=quitar_barra_n(list(linea))
            if(detector_ceros(fila)==1):
                corredores.append(len(fila))
            else:
                corredores.append(maxima_secuencia_ceros(fila))
            
            last_pos=file.tell()
        file.close()
        return max(corredores)                                  #Devolvemos el corredor mas largo.

###########################################################################################################################
#Esta seccion corresponde a la funcion densidad: (puede usar funciones anteriores)

def densidad(file):
        return cantidad_paredes(file)/(dimensiones(file)[0]*dimensiones(file)[1])

###########################################################################################################################
#Esta seccion corresponde a la comunicacion con el usuario: (puede usar funciones anteriores)

try:                                            #Esto es para que si no puede leer el archivo entrada_2, en vez de devolver error, imprima en pantalla el mensaje correspondiente.
        open(entrada_2,'r')
except FileNotFoundError:
        print('No se encuentra un archivo con ese nombre en el directorio actual.')
        sys.exit()                              #Esto termina el sistema, o sea el programa.

if(es_mapa(entrada_2)==True):
        if (entrada_1=='es_mapa' or entrada_1=='cantidad_paredes' or entrada_1=='espacios_rodeados' or entrada_1=='dimensiones' or entrada_1=='corredor_horizontal_mas_largo' or entrada_1=='densidad'):
            if (entrada_1=='es_mapa'):
                    print('Sí, el archivo representa un mapa.')
            if(entrada_1=='cantidad_paredes'):
                    print('El mapa tiene ' + str(cantidad_paredes(open(entrada_2,'r'))) + ' paredes.')
            if(entrada_1=='espacios_rodeados'):
                    print('El mapa tiene ' + str(espacios_rodeados(open(entrada_2,'r'))) + ' huecos rodeados de paredes.')
            if(entrada_1=='dimensiones'):
                    print('El mapa tiene ' + str(dimensiones(open(entrada_2,'r'))[1]) + ' cuadrados de ancho y ' + str(dimensiones(open(entrada_2,'r'))[0]) + ' de alto.')
            if(entrada_1=='corredor_horizontal_mas_largo'):
                    print('El corredor horizontal más largo tiene longitud ' + str(corredor_horizontal_mas_largo(open(entrada_2,'r'))) + '.')
            if(entrada_1=='densidad'):
                    print('La densidad arquitectónica es de ' + str(densidad(open(entrada_2,'r'))) + '.')
        else:
                print('La función ingresada no es correcta.')
else:
        print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')

         
#1) Por que aux=list(f.readline()).remove('\n') me devuelve None?
#cambiar entrada_1, entrada_2 por sys.argv[1], sys.argv[2] resp y borrar las primeras lineas de codigo
