#AA
AA=list(input())
BB=" "
for i in range(len(AA)):
    if BB in AA:
        AA.remove(BB)
print(len(AA))
