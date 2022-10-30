k=0
for i in range(100,1000):

	if int(str(i)[0])+int(str(i)[1])==int(str(i)[2]):

		k=k+1
		print(i)

print("koşulu sağlayan şu kadar sayı vardır= ",k)