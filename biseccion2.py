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
   A=[0]*(iteraciones+2)
   B=[0]*(iteraciones+2)
   A[0]=a
   B[0]=b
   for i in range(iteraciones+1):
      if i!=0:
         if B[i]==B[i-1]:      
            c=float(a*fb-2*b*fa)/(fb-2*fa)
         if A[i]==A[i-1]:      
            c=float(2*a*fb-b*fa)/(2*fb-fa)
         x=c
         fc=eval(s)
         error=(b-a)/2.0
         print i,a,b,c,fa,fb,fc,error
         if fc==0:
            print'La raiz es: ',c
         if fa*fc<0:
            b=c
            fb=fc
            B[i+1]=b
            A[i+1]=a
         else:
            a=c
            fa=fc
            A[i+1]=a
            B[i+1]=b
      if i==0:
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
            B[i+1]=b
            A[i+1]=a
         else:
            a=c
            fa=fc
            A[i+1]=a
            B[i+1]=b
         
       
      #print A
      #print B   
                  
               
         
         
         
#  'x**3-2*sin(x)'
