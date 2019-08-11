    
O=int(input())
K=1
A=1
for j in range(0,O):
  if j!=O-1:
    print(K,end=" ")
  else:
    print(K)
  M=K+A
  K=A
  A=M
