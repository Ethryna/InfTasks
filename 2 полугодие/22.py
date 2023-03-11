with open('Копия 22.txt') as f:
    l = [x for x in f]
    l2 = []
    for i in l:
        l2.append(i.split('\t')[:len(i.split('\t'))-1])
    lens = []
    for pr in l2:
        if pr[2]=='0':
            lens.append(pr[1])
        elif pr[2].count('"')==0:
            lens.append(int(pr[1])+int(lens[int(pr[2])-1]))
        else:
            pr[2] = pr[2][1:len(pr[2])-1]
            procs = pr[2].split('; ')
            prL = []
            for j in range(len(procs)):
                prL.append(int(lens[int(procs[j])-1]))
            addL = max(prL)
            lens.append(int(pr[1])+addL)
    print(max(map(int,lens)))
