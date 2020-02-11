#Llenar un arreglo con potencias de 2
from math import*
n=input('Ingrese el valor de n ')
A=[0]*(n+1)
for i in range(n+1):
   A[i]=2**i
   print A[i]
