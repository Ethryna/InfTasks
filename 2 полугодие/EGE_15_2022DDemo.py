def f(x,a1,a2):
    return (17<=x<=58) <= ((not(29<=x<=80) and not(a1<=x<=a2)) <= (not(17<=x<=58)))
s=[]
for a1 in range(-100,100):
    for a2 in range(-100,100):
        flag=True
        for x in range (-100,100):
            if not(f(x,a1,a2)):
                flag=False
                break
        if flag:
            s.append(a2-a1)
print(min(s))
