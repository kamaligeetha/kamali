import math
P,O=map(int,input().split())
K=0
for i in range(P,O+1):
	U=math.sqrt(i)
	if(U-math.floor(U)==0):
		K=K+1
print(K)
