#Convertir un numero a binario
n=input('Numero de digitos del binario ')
print 'A continuacion ingrese los digitos'
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
   
   
   
   
   
 
