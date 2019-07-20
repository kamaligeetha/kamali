E,D=map(int,input().split())
F=[]
for i in range(E+1,D+1):
    if(i%2!=0):
     F.append(i)
print(*F,sep=" ")
