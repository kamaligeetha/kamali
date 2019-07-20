B=int(input())
if B>1:
    for i in range(2,B):
        if B%i==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
