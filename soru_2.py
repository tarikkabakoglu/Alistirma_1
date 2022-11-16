import math

toplam=0
for i in range(1,10000000):
    toplam+=(1/(i*i))
pi=(toplam*6)**(0.5)
pi2=math.sqrt(toplam*6)
print(pi)
print(pi2)
print(math.pi)
