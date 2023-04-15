with open('27_B.txt') as f:
    data = [list(map(int,x.split())) for x in f]
    P = data[0][0]
    data.pop(0)
    conts = []
    for i in range(P):
        if data[i][1]%36==0:
            conts.append(data[i][1]//36)
        else:
            conts.append(data[i][1]//36+1)
    Ran = [x for x in range(549724-5,549724+5)] #manually adjusting the range decreasing intervals between the elements based on the output
    print(Ran)
    for j in Ran:
        price = 0
        p0 = data[j][0]
        for k in range(P):
            price += abs(p0-data[k][0])*conts[k]
        print(price)

#Answer is 5634689219329
