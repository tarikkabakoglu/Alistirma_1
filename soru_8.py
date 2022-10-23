X=[]

for i in range(1,10):
    
    for y in range(0,10):

        for m in range(0,10,2):

            if i==y:

                sayı=str(i)+str(y)+str(m)
                X.append(int(sayı))

            if i==m:

                sayı=str(i)+str(y)+str(m)
                X.append(int(sayı))

            if y==m:

                sayı=str(i)+str(y)+str(m)
                X.append(int(sayı))

print("koşulu sağlayan bu kadar sayı vardır=",len(X))