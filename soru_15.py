def asal_Mi(x):

	for i in range(2,x):

		if (x%i==0):

			return False

	return True

X=[]

for i in range(10000,100000):

		if (asal_Mi(i)):
		
			X.append(i)
print(X)