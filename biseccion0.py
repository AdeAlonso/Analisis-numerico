#Programa para calcular raices
from math import *
s=input('Function? ')
#x=input('x? ')
#y=eval(s)
#print y
a=input('a? ')
b=input('b? ' )
x=a
fa=eval(s)
if fa==0:
   print'La raiz es: ',a
x=b
fb=eval(s)
if fb==0:
   print'La raiz es: ',b
if fa*fb>0:
   print'Error en los intervalos'
if fa*fb<0:
   e=input('epsilon? ')
   l=(log(b-a)-log(2*e))/log(2)
   print l
   iteraciones=int(ceil(l))
   print('iteraciones: '+str(iteraciones))
   for i in range(iteraciones+1):
      c=float(a*fb-b*fa)/(fb-fa)
      x=c
      fc=eval(s)
      error=(b-a)/2.0
      print i,a,b,c,fa,fb,fc,error
      if fc==0:
         print'La raiz es: ',c
      if fa*fc<0:
         b=c
         fb=fc
      else:
         a=c
         fa=fc
         
         
         
#  'x**3-2*sin(x)'
