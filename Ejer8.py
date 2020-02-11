#Convertir un numero de base 10 a base 2
a=input('Numero? ')
b=int(a)
c=a-b
A=[]
B=[]
C=[]
while b!=0:
   k=b%2
   A.append(k)
   b=(b-k)/2
A.reverse()
A.append('.')
print A
#Convertir un numero decimal a binario

for i in range(52):
   c=2*c
   if c<1:
      B.append(0)
   if c>1:
      B.append(1)
      c=c-1
   if c==1:
      B.append(1)
      break
   print c
print B
d=len(A)
e=len(B)
for i in range(d):
   C.append(A[i])
   print i
for j in range(e):
   C.append(B[j])
   print j
for l in C:
   print l,
print


   
 
