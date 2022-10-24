def palindromik_Mi(x):
    
    for i in range(1,10):
    
        for y in range(0,10):

            if x==int(str(i)+str(y)+str(i)):

                return print("Evet, bu sayı palindromik")

            elif x==int(str(i)+str(y)+str(y)+str(i)):

                return print("Evet, bu sayı palindromik")
   
    return print("Hayır, bu sayı palindromik değil")