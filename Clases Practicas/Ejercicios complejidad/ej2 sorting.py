# PRE: los valores de l estan entre 0 y 9
def sort(l):
	#1. para los numeros entre 0 y 9 contamos cuantos hay de cada uno en l
	cant = [0]*10
	for i in range(len(l)):
		cant[l[i]] = cant[l[i]]+1
	
	#2. escribimos en orden la cantidad que habia de cada un en l
	pos = 0
	for i in range(10):
		for j in range(cant[i]):
			l[pos] = i
			pos = pos+1


l = [2,3,1,3,4,5,9,6,7,4,5,3,2,0,9,7]
print l
sort(l)
print l
