#Posible solucion
#Imprime A
def imprimeMatriz(A):
   n=len(A)
   for i in range(n):
      for j in range(n):
         print '{0:15.5f}'.format(A[i][j]),
      print
   print
   

#Pivoteo parcial
A=input('Matriz? ')
n=len(A)
imprimeMatriz(A)
#k es el indice del pivote
for k in range(n-1):
#Busca maximo
   maximo=abs(A[k][k])
   indice=k
   for i in range(k+1,n):
      absoluto=abs(A[i][k])
      if absoluto>maximo:
         maximo=absoluto
         indice=i
         print i
#Intercambiar filas
   if indice!=k:
      for j in range(k,n):
         temporal=A[k][j]
         A[k][j]=A[indice][j]
         A[indice][j]=temporal
         imprimeMatriz(A)

#Hace ceros hacia abajo
   for i in range(k+1,n):
      factor=-float(A[i][k])/A[k][k]
      for j in range(k,n):
         A[i][j]+=A[k][j]*factor
imprimeMatriz(A)




#                    [[6,-2,2,4],[12,-8,6,10],[5,-13,9,3],[-6,4,1,-18]]

