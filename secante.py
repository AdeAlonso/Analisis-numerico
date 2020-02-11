#Metodo de Secante
from math import *
def f(s,x):
   return eval(s)
u=input('funcion? ')
#v=input('Derivada? ')
a=input('punto1? ')
b=input('punto2? ')
n=input('Iteraciones? ')
B=[0]*(n+1)
for i in range(0,n+1,1):
   if i==0:
      B[0]=a
      if f(u,B[i])==0:
         print 'La raiz es ',B[i]
         break;
      print i,B[i],f(u,B[i])
   if i==1:
      B[1]=b
      if f(u,B[i])==0:
         print 'La raiz es ',B[i]
         break;
      print i,B[i],f(u,B[i])
      
   if i>=2:
      if (f(u,B[i-1])-f(u,B[i-2]))==0:
         print 'La aproximacion es ',B[i]
         break;
      else:
         B[i]=B[i-1]-((B[i-1]-B[i-2])/float(f(u,B[i-1])-f(u,B[i-2])))*f(u,B[i-1])
      #print i,f(u,a),f(v,a),b
         if f(u,B[i])==0:
            print 'La raiz es ',B[i]
            break;
         print i,B[i],f(u,B[i])
      
print B[i]

# 'x**3-x+1'  '3*x**2-1'
# 'x**3-x**2-x-1'    '3*x**2-2*x-1'
# 'x**3-2*x-5'  '3*x**2-x'
# '5*(3*x**4-6*x**2+1)-2*(3*x**5-5*x**3)'   '5*(12*x**3-12*x)-2*(15*x**4-15*x**2)'
# 'x-2*sin(x)'       '2*cos(x)-1'
# 'x**3-sin(x)-7'      '3*x**2-cos(x)' 
# 'sin(x)+x-1'             'cos(x)+1'
# 'x**5-7*x**3-x**2-1'        '5*x**4+2*x-21*x**2'
# 'exp(-1*x**2)-cos(x)-1'          'exp(-1*x**2)*(-2*x)+sin(x)'


# 'x**5+x**3+3'

# 'x**3+2*x**2+10*x-20'   '3*x**2+4*x+10'
