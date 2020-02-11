def imprimeMatriz(A):
   n=len(A)
   for i in range(n):
      for j in range(n):
         print '{0:15.5f}'.format(A[i][j]),
      print
   print


def imprimeVector(b):
   n=len(b)
   for i in range(n):
      print '{0:15.5f}'.format(b[i])
   print

def vectorEscalonamiento(A):
   s=[]
   n=len(A)
   for i in range(n):
      maximo=abs(A[i][0])
      for j in range(n):
         if abs(A[i][j])>maximo:
            maximo=abs(A[i][j])
      s.append(maximo)
   return(s)

def intercambiar(A,inicio,fin):
   a=A.pop(fin)
   A.insert(inicio,a)

def buscarPivote(A,b,s,inicio):
   n=len(A)
   maximo=abs(A[inicio][inicio])/float(s[inicio])
   fin=inicio
   for i in range(inicio+1,n):
      r=abs(A[i][inicio])/float(s[i])
      if r>maximo:
         maximo=r
         fin=i
   if fin!=inicio:
      intercambiar(A,inicio,fin)
      intercambiar(b,inicio,fin)
      intercambiar(s,inicio,fin)

def eliminacionAdelante(A,b):
   n=len(A)
   s=vectorEscalonamiento(A)
   for k in range(n-1):
      buscarPivote(A,b,s,k)
      for i in range(k+1,n):
         f=-float(A[i][k])/A[k][k]
         A[i][k]=0
         for j in range(k+1,n):
            A[i][j]+=f*A[k][i]
         b[i]+=f*b[k]
      imprimeMatriz(A)
      imprimeMatriz(A)
      imprimeVector(s)

def sustitucionAtras(A,b):
   n=len(A)
   X=[0]*n
   for i in range(n-1,-1,-1):
      a=b[i]
      for j in range(i+1,n): 
         a-=A[i][j]*X[j]
      X[i]=a/float(A[i][i])
   return X

A=input('A? ')
b=input('b? ')
eliminacionAdelante(A,b)
X=sustitucionAtras(A,b)
print 'Slucion'
imprimeVector(X)



#                        [[6,-2,2,4],[12,-8,6,10],[5,-13,9,3],[-6,4,1,-18]]          
#    [16,26,-19,-34]
   

   
