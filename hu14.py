K=int(input())
L=list(map(int,input().split()))
P=sorted(L)
A=P[::-1]
U=[]
for i in range(0,len(L)):
	U.append(A[i])
	U.append(P[i])
for j in U[:len(L)]:
	print(j,end=" ")
