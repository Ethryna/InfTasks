L = [x for x in range(1,100)]
d=0
dn = 0
N = []
for k in range(1, len(L)):
    d+=k
for i in L:
    if i%2!=0: N.append(i)
for k in range(1, len(N)):
    dn+=k
print(f'{d-dn} пар')
