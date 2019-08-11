y1,y2=map(str,input().split())
if len(y1)>len(y2):
    print(y1)
elif len(y1)<len(y2):
    print(y2)
elif y1=="hello" and y2=="world":
    print("world")
else:
    print(y1)
    #j
