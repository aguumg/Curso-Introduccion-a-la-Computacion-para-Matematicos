input_list=input('Ingrese los elementos de la lista separados por espacios: ')
A= input_list.split()   #transforma el string del input en una lista, donde cada elemento es cada string
A_aux=[]
i=0
while(i<=len(A)):
        A_aux.append(list(A[:i]))
        i=i+1
print(A_aux)

#La alternativa es poner la lista directamente aca en el programa. Digo, si no
#queremos que nos devuelva los prefijos pero como strings.
