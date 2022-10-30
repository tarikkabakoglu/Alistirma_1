K=121212
for sayi_1 in range(1,121212):

	for sayi_2 in range(1,121212):

		if (sayi_1*sayi_2)==121212:
			
			fark=sayi_1-sayi_2

			if fark>=0 and fark<=K:

				K=fark
				print(sayi_1,sayi_2)