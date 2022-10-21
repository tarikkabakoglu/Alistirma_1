#soru_1

x=sum(range(19,203,3))
print(x)

#soru_2

from math import sqrt

i=0
X=[]
while True:
    i=i+1
    pikare=1/(i**2)
    pi=sqrt(pikare/6)
    X.append(pi)

    if sum(X)>=3.149:
        break

print(sum(X))

#soru_3

def carp(My_list):
    
    result=1   
    for x in My_list:
        result=result * x
    return result

i=0
e=[]

while True:
    i=i+1
    x=1/i
    e.append(x)
    
    if len(e)>100:
        break
print(carp(e))

#soru_4

for i in range(1,10):
    
    for y in range(0,10):

    	print(str(i),str(y),str(i),sep="")

#soru_5

for i in range(1,10):
    
    for y in range(0,10):

        print(str(i),str(y),str(y),str(i),sep="")