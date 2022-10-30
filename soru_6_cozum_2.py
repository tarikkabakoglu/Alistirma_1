X=0

for i in range(1000,10000):
    
    if int(str(i)[0])>int(str(i)[3]):

        X+=1

print(f"altı basamaklı tam sayılardan {X} adedinin ilk basamağındaki sayı son basamağındaki sayıdan büyüktür")