X=0

for i in range(100,1000):

    if str(i)[0]==str(i)[1] or str(i)[1]==str(i)[2] or str(i)[0]==str(i)[2]:

            X+=1
            print(i)

print("koşulu sağlayan bu kadar sayı vardır= ",X)