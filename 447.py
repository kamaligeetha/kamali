K=int(input())
L=list(map(int,input().split()))
for j in range(0,len(L)):
	max1=L[0]
for j in range(0,len(L)):
	if L[j]<max1:
		max1=L[j]
print(max1,end=" ")
for j in range(0,len(L)):
	min1=L[0]
for j in range(0,len(L)):
	if L[j]>min1:
		min1=L[j]
print(min1)
#j
