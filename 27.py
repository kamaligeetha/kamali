L=int(input())
K=L
J=0
while(K>0):
   J=J+(K%10)**3
   K=K//10
if(J==L):
  print('yes')
else:
  print('no')
