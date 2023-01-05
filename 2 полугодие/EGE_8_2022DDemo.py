letters='елмру'
s=[]
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                s.append(a+b+c+d)
print(s.index('леее')+1)
