KL=input()
OO=0
for j in range(0,len(KL)):
  if KL[j].isalnum()==False and KL[j]!=" ":
    OO=OO+1
print(OO)
