#Llenar dos arreglos y sumarlos como vectores
from math import*
n=input('Ingrese la longitud de las listas ')
A=[0]*(n)
B=[0]*(n)
C=[0]*(n)
for i in range(n):
   A[i]=input('Ingrese el valor '+str(i)+' para la lista A ')
for i in range(n):
   B[i]=input('Ingrese el valor '+str(i)+' para la lista B ')
for i in range(n):
   C[i]=(A[i]+B[i])

print A
print B
print 'La lista resultante A+B es '
print C



