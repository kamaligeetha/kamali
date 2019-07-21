M,O=map(int,input().split())
for I in range (M+1,O):
  for N in range (2,I):
    if (I%N==0):
      break
  else:
      print(I,end=" ")
