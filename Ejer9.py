#Convertir un numero a binario
n=input('Numero de digitos del binario antes del punto ')
print 'A continuacion ingrese los digitos antes del punto'
A=[]
for i in range(n):
   k=input('Digito: ')
   A.append(k)
A.reverse()
print A
s=0
for j in range(n):
   if A[j]==1:
      s=s+(2**j)
   if A[j]==0:
      s=s
print s   
   
#Convertir un binario menor que uno a base 10
#n=input('Numero de digitos del binario ')
m=input('Numero de digitos despues del punto ')
print 'A continuacion ingrese los digitos despues del punto'
B=[]
for i in range(m):
   k=input('Digito: ')
   B.append(k)
#B.reverse()
print B
t=0
for j in range(1,m+1,1):
   if B[j-1]==1:
      t=t+(2**(-j))
   if B[j-1]==0:
      t=t
print t
u=s+t
print s
print u
   
   
   


   
    
