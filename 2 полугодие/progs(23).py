from itertools import *
def f1(x,y):
    count = 0
    for i in range(1,10):
        progs = list(product('12',repeat=i))
        for k in progs:
            k1 = ''.join(k)
            t = x
            for c in k1:
                if c =='1': t+=1
                else: t*=2
                if t > y or t==17: break
            if t == y: count+=1
    return(count)

def f2(x,y):
    count = 0
    for i in range(1,24):
        progs = list(product('12',repeat=i))
        for k in progs:
            k1 = ''.join(k)
            t = x
            if k1.count('2')>1:
                continue
            else:
                for c in k1:
                    if c =='1': t+=1
                    else: t*=2
                    if t > y or t==17: break
                if t == y: count+=1
    return(count)
r1 = f1(1,10)
r2 = f2(10,35)
print(r1*r2)

#Ужасное задание



#Нормальный вариант

def f(x,y):
    if x > y or x == 17: return 0
    if x == y: return 1
    else: return f(x+1,y)+f(x*2,y)

print(f(1,10)*f(10,35))

