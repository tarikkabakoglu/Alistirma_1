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