from itertools import *
def f(x,y):
    count = 0
    for i in range(1,y-x+1):
        progs = list(product('12',repeat=i))
        t = x
        for k in progs:
            k1 = ''.join(k)
            for c in k1:
                if c =='1': t+=1
                else: t*=2
                if t > y or t==17: break
                elif t == y: count+=1
    return(count)
r1 = f(1,10)
print(r1)
r2 = f(10,35)
print(r2)
"""for x in range(1,26):
    progs = product('12',repeat=x)
    t = 10
    for k in progs:
        k1 = ''.join(k)
        for c in k1:
            if c =='1': t+=1
            else: t*=2
            if t > 35 or t==17: break
            elif t == 35: count2+=1
            if t == 10: f10 = True
            if t == 17 or t > 35:
                break
            if t == 35: count+=1"""
