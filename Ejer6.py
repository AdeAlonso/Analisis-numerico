#Convertir un numero decimal a binario
n=input('Numero? ')
A=[]
for i in range(10):
   n=2*n
   if n<1:
      A.append(0)
   if n>1:
      A.append(1)
      n=n-1
   if n==1:
      A.append(1)
      break
   print n
print A
