A,B,C=map(str,input().split())
A=list(A)
B=list(B)
C=int(C)
count=0
for i in range(0,len(A)):
	if(A[i]!=B[i]):
		count=count+1
if(count==C):
	print("yes")
else:
	print("no")
