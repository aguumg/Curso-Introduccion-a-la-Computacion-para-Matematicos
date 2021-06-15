import sys

# esta funcion decide si es un rectangulo
def es_rectangulo(nombre):
  f=open(nombre,'r')
  M = f.readlines()
  f.close()
  # cuento la cantidad de lineas con la misma longitud que la ultima mas uno (porque el \n no esta)
  s = len(M)
  b = 0 #contador
  j = 0
  while j < s:
    if len(M[j]) == len(M[len(M)-1])+1:
      b = b + 1
    j = j + 1
  return s == b+1

# esta funcion verifica si solo hay ceros y unos (eventualmente \n)
def tiene_solo_ceros_y_unos(nombre):
  f=open(nombre,'r')
  x = f.read()
  f.close()
  s = len(x)
  b = 0
  i = 0
  while i < s:
    if x[i] in ['0', '1', '\n']:
      b = b + 1
    i = i + 1
  return s == b

def es_mapa(nombre):
  a = es_rectangulo(nombre)
  b = tiene_solo_ceros_y_unos(nombre)
  return a and b

def dimensiones(nombre):
  f = open(nombre,'r')
  M = f.readlines()
  ancho = len(M[len(M)-1])
  alto = len(M)
  f.close()
  return [ancho, alto]

def cantidad_paredes(nombre):
  f = open(nombre,'r')
  x = f.read()
  s = len(x)
  f.close()
  paredes = 0 #contador
  j = 0
  while j < s:
    if x[j] == '1':
      paredes = paredes + 1
    j = j+1
  return paredes

def densidad(nombre):
  f = open(nombre,'r')
  x = f.read()
  s = len(x)
  f.close()
  espaciototal = 0 #contador
  i = 0
  while i < s:
    if not x[i] == '\n':
      espaciototal = espaciototal + 1
    i = i + 1
  return cantidad_paredes(nombre)/espaciototal

# esta funcion auxiliar calcula el corredor mas largo para cada fila del mapa
def cml(fila):
  # guardo en un arreglo A las posiciones donde hay un 1
  s = len(fila)
  A = []
  i = 0
  while i < s:
    if fila[i] in ['1', '\n']:
      A = A + [i]
    i = i + 1
  #print(A)
  # guardo en otro arreglo B las distancias entre cada posicion
  corredor_mas_largo = 0  
  l = len(A)
  B = []
  j = 0
  while j < l-1:
    B = B + [A[j+1] - A[j] - 1]
    j = j + 1
  B = [A[0]] + B
  #print(B)
  # busco la distancia maxima (que es el maximo del arreglo B)    
  k = 0
  while k < l:
    if B[k] >= corredor_mas_largo:
      corredor_mas_largo = B[k]
    k = k + 1
  return corredor_mas_largo

def corredor_horizontal_mas_largo(nombre):
  f = open(nombre,'r')
  alto = dimensiones(nombre)[1]
  i = 1
  chml = 0
  while(i < alto):
    x = f.readline()
    #print(x)
    #print(cml(x))
    if cml(x) >= chml:
      chml = cml(x)
    i = i + 1
  # la ultima linea es la unica que no termina en \n, hay que hacerlo aparte
  y = f.readline()+'\n'
  #print(y)
  #print(cml(y))
  if cml(y) >= chml:
    chml = cml(y)
  return chml

def espacios_rodeados(nombre):
  f = open(nombre,'r')
  M = f.readlines()
  ancho = dimensiones(nombre)[0]
  alto = dimensiones(nombre)[1]
  esp_rod = 0
  j = 1
  while j <= alto-2:    
    i = 1
    while i <= ancho-2:
      #print(M[j][i])
      if M[j][i] == '0' and M[j-1][i-1] == M[j][i-1] == M[j+1][i-1] == M[j-1][i] == M[j+1][i] == M[j-1][i+1] == M[j][i+1] == M[j+1][i+1] == '1':
        esp_rod = esp_rod + 1
      i = i + 1
    j = j + 1
  return esp_rod


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
