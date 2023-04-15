with open('26.txt') as f:
    data = [list(map(int,x.split())) for x in f]
    psc = data[1][0]
    cells = data[0][0]
    data = sorted(data[2:])
    free = [x for x in range(1,211)]
    locked = []
    c = 0
    last = 0
    for i in data:
        for j in locked:
            if j[1]<i[0]:
                free.append(j[0])
                locked.pop(locked.index(j))
        if free:
            locked.append([min(free),i[1]])
            last = min(free)
            free.pop(free.index(min(free)))
            c+=1            
    print(c, last)

    
    
