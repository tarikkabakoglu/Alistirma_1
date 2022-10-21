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