P,L=map(int,input().split())
for i in range(P,L):
  su=0
  temp=i
  while(temp>0):
     su=su+(temp%10)**3
     temp=temp//10
  if(su==i):
     print(i,end=" ")
