'''with open('27A.txt') as f:
    data = [int(x) for x in f]
    N = data[0]
    K = data[1]
    data.pop(0)
    data.pop(0)
    Sm = 0
    for i in range(N):
        for k in range(i+24,N):
            s = data[i]+data[k]
            Sm = max(s,Sm)
    print(Sm)'''



with open('27B.txt') as f:
    data = [int(x) for x in f]
    N = data[0]
    K = data[1]
    data.pop(0)
    data.pop(0)
    datah = data
    maxs = []
    maxind = []
    for i in range(10):
        maxs.append(max(datah))
        maxind.append(data.index(max(datah)))
        datah.pop(datah.index(max(datah)))
    Sm = 0
    for i in range(9):
        if abs(maxind[i]-maxind[i+1])>=K:
            Sm = max(Sm, maxs[i]+maxs[i+1])
    print(Sm)
