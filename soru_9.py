X=[]

for i in range(1,10):
    
    for y in range(0,10):

        for m in range(0,10):

            if (i+y+m)<9:

                sayı=str(i)+str(y)+str(m)
                X.append(int(sayı))

print(X)    
print("koşulu sağlayan bu kadar sayı vardır=",len(X))