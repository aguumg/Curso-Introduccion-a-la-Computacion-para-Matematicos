def concatenar(c,A):
	RV=[]
	for x in A:
		RV=RV+[c,x]
	return RV

def permut(A):
	RV=[]
	if(len(A)==1):
		RV=[A[0]]
	else:
		for c in A:
			index=A.index(c)
			A.remove(c)
			RV=RV+[concatenar(c,permut(A))]
			A.insert(index,c)
	return RV
A=[1,2,3]
print(permut(A))


