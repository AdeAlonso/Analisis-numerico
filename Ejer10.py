#Programa para hacer eliminacion hacia adelante.
#Funcion para imprimir matriz
def imprimeMatriz(A):
      for fila in A:
         for elemento in fila:
            print elemento,'\t',
         print

A=input('A? ')
n=len(A)
#i=0
S=input('B? ')
for i in range(n):
  l=i+1
  q=i
 
  for j in range(l,n,1):
      p=float(-A[j][i])/A[i][i]
      #print A[j][i]
      for k in range(q,n,1):
        A[j][k]=p*A[i][k]+A[j][k]   
      #print p
      #imprimeMatriz(A)
      l=l+1
      S[j]=p*S[i]+S[j]
      
      #print 
  print S   
   #S.happend()
imprimeMatriz(A)


#[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]
#[16,26,-19,-34]
