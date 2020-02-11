#Metodo de Newton-Raphso
from math import *
def f(s,x):
   return eval(s)
u=input('funcion? ')
v=input('Derivada? ')
a=input('Aproximacion? ')
n=input('Iteraciones? ')
b=0
for i in range(n+1):
   if i==0:
      b=a
      print i,b,f(u,b)
   else:
      b=a-(f(u,a)/float(f(v,a)))
      #print i,f(u,a),f(v,a),b
      print i,b,f(u,b)
      a=b
print b

# 'x**3-x+1'  '3*x**2-1'
# 'x**3-x**2-x-1'    '3*x**2-2*x-1'
# 'x**3-2*x-5'  '3*x**2-x'
# '5*(3*x**4-6*x**2+1)-2*(3*x**5-5*x**3)'   '5*(12*x**3-12*x)-2*(15*x**4-15*x**2)'
# 'x-2*sin(x)'       '2*cos(x)-1'
# 'x**3-sin(x)-7'      '3*x**2-cos(x)' 
# 'sin(x)+x-1'             'cos(x)+1'
# 'x**5-7*x**3-x**2-1'        '5*x**4+2*x-21*x**2'
# 'exp(-1*x**2)-cos(x)-1'          'exp(-1*x**2)*(-2*x)+sin(x)'
