
import numpy as np
import random 

#1
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
for i in lista:
    lista2.append(-i)
print("1. ",lista2)

#2
mat = np.random.random((3,3))
print("2. ", mat)

#3
A = np.random.randint((3,3))
B = np.random.randint((3,1))
C = np.random.randint((3,1))
print("3. ", A+B+C)

#4
numbers = list(range(1, 101))

for i in range(len(numbers)):
    if numbers[i] % 3 == 0:
        numbers[i] = "m3"

print(numbers)


#5
