X=[]

for i in range(1,10):
    
    for y in range(0,10):

        for m in range(0,10):

            for t in range(0,10):

                if t<i:

                    sayı=str(i)+str(y)+str(m)+str(t)
                    X.append(int(sayı))
                    
print(len(X))                  