# PRE: l1 y l2 estan ordenadas y no tienen elementos repetidos
# Devuelve la cantidad de elementos que aparecen en ambas listas
def enAmbasListas(l1, l2):
	rv = 0
	i = 0
	j = 0
	while i<len(l1) and j<len(l2):
		if l1[i]==l2[j]:
			rv = rv+1
			i = i+1
			j = j+1
		elif l1[i]<l2[j]:
			i = i+1
		else:
			j = j+1
	return rv

print enAmbasListas([1,2,3,4,5], [1,5,6,7,8])
print enAmbasListas([5], [1,6,7,8])
print enAmbasListas([1,6,7,8], [1,6,7,8])
