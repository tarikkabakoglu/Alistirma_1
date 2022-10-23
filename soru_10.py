X=[]

for i in range(1,10):
    
    for y in range(0,10):

        for m in range(0,10):

            for t in range(0,10):

                for z in range(0,10):

                    if str(i)+str(y)==str(t)+str(z):

                        sayı=str(i)+str(y)+str(m)+str(t)+str(z)
                        X.append(int(sayı))
                        
print("koşulu sağlayan bu kadar sayı vardır=",len(X))