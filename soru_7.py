X=[]

for i in range(1,10):
    
    for y in range(0,10):

        for m in range(0,10):

            if (i+y)==m:

                sayı=str(i)+str(y)+str(m)
                X.append(int(sayı))
                print(int(sayı))


print("koşulu sağlayan bu kadar sayı vardır=",len(X))