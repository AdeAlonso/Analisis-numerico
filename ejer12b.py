#Factorizacion LU

def imprimeMatriz(A):
   n=len(A)
   for i in range(n):
      for j in range(n):
         print '{0:15.5f}'.format(A[i][j]),
      print
   print
   

A=input('Matriz? ')
n=len(A)
imprimeMatriz(A)
M=[]
for i in range(n):
   M.append([])
   for j in range(n):
      if j==i:
         M[i].append(1)
      else:
         M[i].append(0)
imprimeMatriz(M)
#Hace ceros hacia abajo   
for k in range(n):
   for i in range(k+1,n):
      factor=-float(A[i][k])/A[k][k]
      print factor
      M[i][k]=-factor
      #if i==k:
       #     M[k][i]=1 
      for j in range(k,n):
         A[i][j]+=A[k][j]*factor

imprimeMatriz(A)
imprimeMatriz(M)


#                    [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
#    [16,26,-19,-34]
