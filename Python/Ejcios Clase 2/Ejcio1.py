filename=input('Ingrese el nombre del archivo junto a su formato: ')
#El archivo que leamos debe estar en el directorio de este archivo!
f=open(filename,'r')
i=0
#f.seek(0) resetea el puntero (para poder releer sin volver a abrir)
for linea in f:
        if((linea.lstrip('\t')).startswith('\n')==False and (linea.lstrip('\t')).startswith('#')==False):
                print (linea)
                i=i+1
print (i)

