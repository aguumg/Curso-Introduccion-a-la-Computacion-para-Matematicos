from mapa import Mapa #Importo el TAD Mapa

ej1 = Mapa("siguiendoPared.txt")
ej2 = Mapa("Emptiness.txt")
ej3 = Mapa("Inalcanzable.txt")
ej4 = Mapa("Pasillos.txt")
ej5 = Mapa("MuchasSoluciones.txt")

#mapa_copia = ej1.dar_copia()
#mapa_copia.escribir_en_posicion(2,2,9)


def resolver_mapa_recursivamente(objeto_mapa, pos_inicial, pos_destino):
    """Si es posible llegar desde la pos_inicial (n_fila, n_columna) hasta
    la pos_destino, devuelve True y un Mapa con el recorrido marcado mediante
    el símbolo 2
    Si no es posible, devuelve False y un Mapa donde todas las posiciones alcanzables
    desde el inicio han sido marcadas con 2

    Métodos o propiedades de Mapa usados:
        ESPACIO_VACIO # El símbolo que representa espacio vacio
        PARED_SOLIDA  # El símbolo que representa pared
        es_posicion_valida(self, i, j)
        posicion(self, i, j) #Devuelve el valor de esa posición    
        escribir_en_posicion(self,i,j,simbolo) # Nuevo, no está en el TAD original
        representar_mapa_con_explorador(self, fila_explorador, columna_explorador, direccion_explorador="ninguna") # Nueva, unicamente para ver el recorrido del algoritmo
    """
    salida_encontrada = False
    ESPACIO_RECORRIDO = 2 # Simbolo que uso para marcar espacios vacíos ya recorridos
    #nuevo_mapa = objeto_mapa.dar_copia()
    
    inicial_fila = pos_inicial[0]
    inicial_columna = pos_inicial[1]
    destino_fila = pos_destino[0]
    destino_columna = pos_destino[1]
    # Recordar que asumimos que la posición inicial es válida, no es una pared
    # Marcamos el espacio inicial como recorrido
    objeto_mapa.escribir_en_posicion(inicial_fila, inicial_columna, ESPACIO_RECORRIDO)
    # Parte "gráfica"
    objeto_mapa.representar_mapa_con_explorador(inicial_fila, inicial_columna)
    if (pos_inicial == pos_destino):
        salida_encontrada = True
        print("Salida encontrada!")
    else:
        # Ahora tratemos de movernos en las 4 direcciones
        diccionario_posicion_a_probar = {"arriba": (inicial_fila - 1, inicial_columna),
                                         "abajo": (inicial_fila + 1, inicial_columna),
                                         "izquierda": (inicial_fila, inicial_columna - 1),
                                         "derecha": (inicial_fila, inicial_columna + 1)}
        posibles_direcciones = list(diccionario_posicion_a_probar.keys())
        i = 0
        # Voy a ir probando en qué dirección puedo ir. Apenas encontré una salida yendo por una, termino
        while (i < len(posibles_direcciones) and (not salida_encontrada)):
            posicion_a_probar = diccionario_posicion_a_probar[posibles_direcciones[i]]
            fila_a_probar = posicion_a_probar[0]
            columna_a_probar = posicion_a_probar[1]
            # Si esa dirección tiene un espacio vacio, resuelvo recursivamente empezando desde ahí
            if (objeto_mapa.es_posicion_valida(fila_a_probar, columna_a_probar) and objeto_mapa.posicion(fila_a_probar , columna_a_probar) == objeto_mapa.ESPACIO_VACIO):
                salida_encontrada, mapa_recorrido = resolver_mapa_recursivamente(objeto_mapa, (fila_a_probar, columna_a_probar), pos_destino)
            i = i + 1
    return salida_encontrada, objeto_mapa


resolver_mapa_recursivamente(ej1, (0,6), (2,2))
#resolver_mapa_recursivamente(ej2, (0,0), (10,5))
#print((not resolver_mapa_recursivamente(ej3, (0,0), (10,5))[0])*"No hay salida!")
# resolver_mapa_recursivamente(ej4, (0,0), (10,5))

















# Qué pasa si queremos devolver todas las soluciones? (Con trayectorias que no repiten posiciones internas)
# Peligroso, facilmente puede haber cantidades exponenciales, supraexponenciales, o peor

# Código feo, usar bajo el propio riesgo
def resolver_mapa_recursivamente_all_solutions(objeto_mapa, pos_inicial, pos_destino):
    """Output: salida_encontrada (Boolean), lista_soluciones(lista de Mapas, [] si salida_encontrada es False)
    Como tercer output, mapa_obtenido, da un mapa con un trayecto tomado sin salida en caso que no se la encuentre"""
    salida_encontrada = False
    ESPACIO_RECORRIDO = 2 # Simbolo que uso para marcar espacios vacíos ya recorridos
    #####################################
    nuevo_mapa = objeto_mapa.dar_copia() # Crea un nuevo mapa
    #####################################
    mapa_obtenido = nuevo_mapa.dar_copia()
    lista_de_mapas_solucion = []
    
    inicial_fila = pos_inicial[0]
    inicial_columna = pos_inicial[1]
    destino_fila = pos_destino[0]
    destino_columna = pos_destino[1]
    # Recordar que asumimos que la posición inicial es válida, no es una pared
    # Marcamos el espacio inicial como recorrido
    nuevo_mapa.escribir_en_posicion(inicial_fila, inicial_columna, ESPACIO_RECORRIDO)
    # Parte "gráfica"
    nuevo_mapa.representar_mapa_con_explorador(inicial_fila, inicial_columna)
    if (pos_inicial == pos_destino):
        salida_encontrada = True
        lista_de_mapas_solucion.append(nuevo_mapa)
        mapa_obtenido = nuevo_mapa
        print("Salida encontrada!")
    else:
        # Ahora tratemos de movernos en las 4 direcciones
        diccionario_posicion_a_probar = {"arriba": (inicial_fila - 1, inicial_columna),
                                         "abajo": (inicial_fila + 1, inicial_columna),
                                         "izquierda": (inicial_fila, inicial_columna - 1),
                                         "derecha": (inicial_fila, inicial_columna + 1)}
        posibles_direcciones = list(diccionario_posicion_a_probar.keys())
        i = 0
        # SACO DE LA GUARDA LA RESTRICCION DE SALIDA NO ENCONTRADA
        while (i < len(posibles_direcciones)):
            salida_encontrada_por_este_camino = False
            posicion_a_probar = diccionario_posicion_a_probar[posibles_direcciones[i]]
            fila_a_probar = posicion_a_probar[0]
            columna_a_probar = posicion_a_probar[1]
            # Si esa dirección tiene un espacio vacio, resuelvo recursivamente empezando desde ahí
            if (nuevo_mapa.es_posicion_valida(fila_a_probar, columna_a_probar) and nuevo_mapa.posicion(fila_a_probar , columna_a_probar) == nuevo_mapa.ESPACIO_VACIO):
               salida_encontrada_por_este_camino, soluciones_por_aca, mapa_por_este_camino = resolver_mapa_recursivamente_all_solutions(nuevo_mapa, (fila_a_probar, columna_a_probar), pos_destino)
               #print(salida_encontrada_por_este_camino, soluciones_por_aca)
               if (salida_encontrada_por_este_camino):
                   salida_encontrada = True
                   #print(lista_de_mapas_solucion)
                   lista_de_mapas_solucion.extend(soluciones_por_aca)
               else:
                    mapa_obtenido = mapa_por_este_camino
                    nuevo_mapa = mapa_obtenido # Asi en siguientes ciclos del while ya no vuelvo a recorrer eso
            i = i + 1
    return salida_encontrada, lista_de_mapas_solucion, mapa_obtenido

#print((not resolver_mapa_recursivamente_all_solutions(ej3, (0,0), (10,5))[0])*"No hay salida!")
#print(resolver_mapa_recursivamente_all_solutions(ej4, (0,0), (10,5)))
#print(resolver_mapa_recursivamente_all_solutions(ej5, (0,0), (0,3)))
