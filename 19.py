T,S=map(int,input().split())
arr=[]
arr=[int(i) for i in input().split()]
A=0
NUM=0
while S>0:
  NUM+=arr[A]
  S=S-1
  A=A+1
print(NUM)
