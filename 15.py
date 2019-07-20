A,B,K =input().split()
A=int(A)
B=int(B)
K=int(K)
if (A>=B and A>=K):
  print (A)
elif (B>=A and B>=K):
  print (B)
else:
  print (K)
