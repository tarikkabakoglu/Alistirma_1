import math

toplam=1 #0!=1 olduğu için 1 ekledik
faktöriyel=1 
for i in range(1,100000):
	faktöriyel*=i
	toplam+=(1/(faktöriyel))
e=toplam
print(e)
print(math.e)
