#Llenar un arreglo con potencias de 2, sumar sus entradas e imprimir el resultado.
from math import*
n=input('Ingrese el valor de n ')
A=[0]*(n+1)
s=0
for i in range(n+1):
   A[i]=2**i
   s+=A[i]
print A
print(s)

