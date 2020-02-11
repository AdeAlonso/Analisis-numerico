#Imprime A
def imprimeMatriz(A):
   n=len(A)
   for i in range(n):
      for j in range(n):
         print '{0:15.5f}'.format(A[i][j]),
      print
   print
 
A=input('A? ')
b=input('b? ')
c=input('Solucion inicial? ')
N=input('Iteraciones? ')
n=len(A)
D=[0]*n
for i in range(N):
   for j in range(n):
      s=0
      for k in range(n):
        # if k==j:
        #       continue
        s=s+A[j][k]*c[k]
        # s=s+A[j][k]*c[k]
      #D[j]=float(b[j]-s)/A[j][j]
      D[j]=float(b[j]-s+A[j][j]*c[j])/A[j][j]
   c=D[:]
   print c
   

         
         
         
       
#         [[2,-1,0],[-1,3,-1],[0,-1,2]]
#         [1,8,-5]
#         [0,0,0]
