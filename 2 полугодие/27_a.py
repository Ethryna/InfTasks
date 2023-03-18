with open('27-B_1.txt') as f:
    n = int(f.readline())
    P = [list(map(int,x.split())) for x in f]
    ds = []
    ms = []
    for i in P:
        ds.append(abs(i[0]-i[1]))
        ms.append(max(i))
    ans = sum(ms)
    print(ans)
    if ans%5==0:
        ans -= min(ds)
    print(ans)
    
