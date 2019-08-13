P=int(input())
for j in range(0,100):
	if 2**j==P:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("yes")
else:
	print("no")
  #j
