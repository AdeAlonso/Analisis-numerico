#Imprime matriz

print 'Programa de reconocimiento de patrones supervisado: Distancia minima'
#A=input('Ingrese objetos  ')
G1=input('Ingrese clase 1 ')
G2=input('Ingrese clase 2 ')
G3=input('Ingrese clase 3 ')
#n=len(A)
g1=len(G1)
g2=len(G2)
g3=len(G3)
Z1=[0]*(2)
Z2=

z1=0
z2=0
#print n

for i in range(g1):
	z1=z1+G1[i][0]
Z1[0]=float(z1)/g1
for i in range(g1):
	z2=z2+G1[i][1]
Z1[1]=float(z2)/g1
print Z1
	
 




#A=[[8,9],[5,3],[7,6],[2,4],[6,1],[3,5],[8,6],[1,3],[4,7],[8,3],[1,1]]
#G1= [[8,9],[7,6],[8,6],[8,3]]
#G2= [[6,1],[1,3],[1,1]]
#G3= [[5,3],[2,4],[3,5],[4,7]]

