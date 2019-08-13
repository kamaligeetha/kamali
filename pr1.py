N=int(input())
L=[]
for k in range(N):
	S=input()
	L.append(S)
T=min(L)
D=len(T)
for k in range(1,D+1):
	
	A=T[0:k]
	if all(A==i[0:k] for i in L):
		X=A
print(X)
