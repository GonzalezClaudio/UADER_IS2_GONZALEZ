import matplotlib.pyplot as plt
import numpy as np
import sys
import random

def collatz(num):
    cont=0
    
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        cont+=1
        
        
    return cont 

secuencia = collatz(11)

print(secuencia)
x=[]
y=[]
for i in range(1,100):
    x.append(i)
    y.append(collatz(i))


plt.plot(x, y)
plt.show()



