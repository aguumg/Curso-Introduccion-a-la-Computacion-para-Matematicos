import sys

def quitar_barra_n(lista):                              #Esto es porque cada salto de renglon se lee como \n al final de la linea, y eso no lo queremos en la lista, asi que lo borramos. (De las listas que lo tienen, porque list.remove nos tira error si no hay nada)
        if('\n' in lista):                      
                lista.remove('\n')
        return lista

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


class Mapa:
    def __init__(self, nombre_archivo):
        self.map=open(nombre_archivo,'r')

    def alto(self):
        self.map=open(self.map.name,'r')
        filas_mapa=self.map.readlines()
        self.map.close()
        return len(filas_mapa)
    
    def ancho(self):
        self.map=open(self.map.name,'r')
        filas_mapa=self.map.readlines()
        self.map.close()
        return len(quitar_barra_n(list(filas_mapa[0])))

    def es_posicion_valida(self,pos):
        bool_final=True
        if(pos[0]>self.alto() or pos[1]>self.ancho()):
            bool_final=False
        return bool_final

    def posicion(self,pos):
#pos=[n° fila,n° columna], donde arrancamos a contar desde 0.
        self.map=open(self.map.name,'r')
        filas_mapa=self.map.readlines()
        return filas_mapa[pos[0]][pos[1]]

    def cantidad_paredes(self):
        self.map=open(self.map.name,'r')
        contador=0
        filas_mapa=self.map.readlines()
        i=0
        while(i<len(filas_mapa)):
            indice=0
            fila=quitar_barra_n(list(filas_mapa[i]))
            while(indice<len(fila)):                                #Recorro todos los elementos de la fila i-ésima, contando cada 1 que tenga.
                if(fila[indice]=='1'):
                    contador=contador+1
                indice=indice+1
            i=i+1
        self.map.close()
        return contador

    def corredor_horizontal_mas_largo(self):
        self.map=open(self.map.name,'r')
        corredores=[]
        filas_mapa=self.map.readlines()
        i=0
        while(i<len(filas_mapa)):
            fila=quitar_barra_n(list(filas_mapa[i]))
            if(detector_ceros(fila)==1):
                corredores.append(len(fila))
            else:
                corredores.append(maxima_secuencia_ceros(fila))
            i=i+1
        self.map.close()
        return max(corredores)

    def densidad_arquitectonica(self):
        return self.cantidad_paredes()/(self.alto()*self.ancho())

