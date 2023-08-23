


import numpy as np


numeros = [5, -2, 10, -8, 3, -6, 8]

valores_negativos = [numero for numero in numeros if numero < 0]

print(valores_negativos)



#2


matriz= np.random.rand(3,3)

print(matriz)


#3


B = np.random.randint(3,1)


C = np.random.randint(3,1)


result= matriz*B + C

print(result)



