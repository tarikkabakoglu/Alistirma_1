X=[]

for sayi_1 in range(1,1000):

	for sayi_2 in range(1,1000):

		fark=sayi_1-sayi_2

		if (sayi_1*sayi_2)==121212:
			
			X.append(fark)

			if fark == min(X):

				print("sayı 1=",sayi_1,"sayı 2=",sayi_2)
				print("en büyük fark=",min(X))