#Convertir un binario menor que uno a base 10
n=input('Numero de digitos del binario ')
print 'A continuacion ingrese los digitos despues del punto'
A=[]
for i in range(n):
   k=input('Digito: ')
   A.append(k)
A.reverse()
print A
s=0
for j in range(1,n+1,1):
   if A[j-1]==1:
      s=s+(2**(-j))
   if A[j-1]==0:
      s=s
print s   
   
   
   
   
   
 
