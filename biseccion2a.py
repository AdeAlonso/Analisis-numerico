#falsa posicion modificado
from math import *
def f(s,x):
   return eval(s)
s=input('f? ')
a=input('a? ')*1.0
b=input('b? ')*1.0
n=input('n? ')
fa=f(s,a)
fb=f(s,b)
if fa==0:
   print 'raiz= ',a
if fb==0:
   print 'raiz= ',b
if fa*fb>0:
   print 'error'
if fa*fb<0:
   c=(a*fb-b*fa)/float(fb-fa)
   for i in range(n+1):
      fc=f(s,c)
      print i,a,b,c,fa,fb,fc
      if fc==0:
         print 'raiz = ',c
         break
      if fa*fc<0:
         b=c
         fb=fc
         c=(2*a*fb-b*fa)/float(2*fb-fa)
      else:
         a=c
         fa=fc
         c=(a*fb-2*b*fa)/float(fb-2*fa) 



#  'x**3-2*sin(x)'
