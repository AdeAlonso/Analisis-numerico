#Imprime A
def imprimeMatriz(A):
   n=len(A)
   for i in range(n):
      for j in range(n):
         print '{0:15.5f}'.format(A[i][j]),
      print
   print

#A=input('A? ')
#b=input('b? ')
N=input('longitud? ')
#n=len(A)
#D=[0]*n
 
G=[0]*N
#Genera las lista que queremos 
B=[]
C=[]
D=[]
E=[]
F=[]
for i in range(N):
   B.append(i+1)
   C.append(5)
   if i>=1 and i<=N-1:
      E.append(-1)
      F.append(-1)
      C[i]=C[i]-(F[i-1]/C[i-1])*E[i-1]
      B[i]=B[i]-(F[i-1]/C[i-1])*B[i-1]
#Sustitucion hacia atras
for i in range(N-1):
   G[N-1-i]=B[N-1-i]-E[N-i]/C[i]
   
print B
print C
print len(C)
print E
print len(E)
print F
print len(F)
print G
#Hace ceros hacia abajo
#for i in range(k+1,n):
#   factor=-float(A[i][k])/A[k][k]
#   for j in range(k,n):
#      A[i][j]+=A[k][j]*factor
#imprimeMatriz(A)

   

         
         
          
       
#         [[2,-1,0],[-1,3,-1],[0,-1,2]]
#         [1,8,-5]
#         [0,0,0]
