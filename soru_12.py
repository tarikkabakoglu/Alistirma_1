for i in range(1,10):
    
    for y in range(0,10):

        for m in range(0,10):

            for t in range(0,10):

                sayı=str(i)+str(y)+str(m)+str(t)
                
                if i+y+m+t==(2005-int(sayı)):

                    print(f"{sayı} yılında doğmuştur")