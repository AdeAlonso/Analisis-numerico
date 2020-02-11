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
S=[0]*n
T=[0]*n
imprimeMatriz(A)
#Busca maximo
maximo=abs(A[0][0])
indice=0
S[0]=maximo
for i in range(n):
   for j in range(n):
      absoluto=abs(A[i][j])
      if absoluto>=maximo:
         maximo=absoluto
         indice=i
         S[i]=maximo
         #print i
print S
for k in range(n):
#k es el indice del pivote
#for k in range(n-1):
#Dividir
   for i in range(k,n):
      T[i]=abs(float(A[i][k])/S[i])
#Encuentra el mas grande del vector de division
   maximo1=abs(T[k])
   indice1=k
   for l in range(k,n):
      absoluto1=abs(T[l])
      if absoluto1>maximo1:
         maximo1=absoluto1
         indice1=l
   print T
   print indice1
   print maximo1    
   

#Intercambiar filas
   if indice1!=k:
      temporal=A[k]
      A[k]=A[j]
      A[j]=temporal
      temporal1=S[k]
      S[k]=S[j]
      S[j]=temporal1
   imprimeMatriz(A)
   print S

#Hace ceros hacia abajo
   for i in range(k+1,n):
      factor=-float(A[i][k])/A[k][k]
      for j in range(k,n):
         A[i][j]+=A[k][j]*factor
   imprimeMatriz(A)




#                    [[6,-2,2,4],[12,-8,6,10],[5,-13,9,3],[-6,4,1,-18]]
#    [16,26,-19,-34]

