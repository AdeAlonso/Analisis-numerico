import math
print 'Programa de reconocimiento de patrones supervisado: Distancia minima'
A=input('Ingrese los objetos: ')
n=input('Numero de clases? ')
G=[]
H=[]*(n)
for i in range(1,n+1,1):
    S=input('Ingresa la clase '+str(i)+': ')
    G.append(S)
    m=len(S)
    T=[0,0]
    for j in range(2):
        for k in range(m):
            T[j]=T[j]+float(S[k][j])/m
    #print T
    H.append(T)
print H
m=input('Numero de objetos nuevos? ')
for i in range(1,m+1,1):
   R=input('Ingrese el objeto nuevo '+str(i)+': ')
   l=len(R)
   #print k
#Comparar
   D=[0]*(n)
   for j in range(n):
      for k in range(l):
         D[j]=D[j]+(R[k]-H[j][k])**2
      D[j]=math.sqrt(D[j])
   minimo=D[0]
   indice=0
   for j in range(n):
      if D[j]<minimo:dddd
         minimo=D[j]
         indice=j
   #print indice
   clase=indice+1
   #print minimo
      
   #print D    
   #print R
   print ('Objeto '+str(i)+' pertenece a la clase '+str(clase))





#A=        [[8,9],[5,3],[7,6],[2,4],[6,1],[3,5],[8,6],[1,3],[4,7],[8,3],[1,1]]
#G1=       [[8,9],[7,6],[8,6],[8,3]]
#G2=       [[6,1],[1,3],[1,1]]
#G3=       [[5,3],[2,4],[3,5],[4,7]]
 
            
#  [[1,1],[1,0],[2,3],[4,5],[5,4]]
#  [[2,3],[4,5],[5,4]]
#  [[1,1],[1,0]]
#  [2,2]
