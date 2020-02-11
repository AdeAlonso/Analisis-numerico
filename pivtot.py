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
for k in range(n):
#Busca maximo
   maximo=abs(A[k][k])
   fila=k
   columna=k
   for j in range(n):
      for i in range(k,n):
         absoluto=abs(A[i][j])
         if absoluto>maximo:
            maximo=absoluto
            fila=i
            columna=j
            print i
   print fila
   print columna
   print maximo
  



#Intercambiar filas
   if fila!=k:
      for j in range(k,n):
         temporal=A[k][j]
         A[k][j]=A[fila][j]
         A[fila][j]=temporal
#Intercambiar columnas
   if columna!=k:
      for j in range(k,n):
         guardar=A[j][k]
         A[j][k]=A[j][columna]
         A[j][columna]=guardar 
      
   
         
   imprimeMatriz(A)

#Hace ceros hacia abajo
   for i in range(k+1,n):
      factor=-float(A[i][k])/A[k][k]
      for j in range(k,n):
         A[i][j]+=A[k][j]*factor
imprimeMatriz(A)




#                    [[6,-2,2,4],[12,-8,6,10],[5,-13,9,3],[-6,4,1,-18]]

