#Convertir un numero de base 10 a base 2
a=input('Numero? ')
A=[]
while a!=0:
   k=a%2
   A.append(k)
   a=(a-k)/2
A.reverse()
print A

