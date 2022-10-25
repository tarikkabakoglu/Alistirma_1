A=[]

for X in range(1,350):

	if 125%X==200%X==350%X:

		A.append(X)
print(max(A))