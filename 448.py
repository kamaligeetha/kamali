N=int(input())
sum=0
P=list(map(int,input().split()))
for j in range(0,len(P)):
	sum=sum+P[j]
avg=sum//N
print(avg)
#j
