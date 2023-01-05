cost_punkt=[]
data=[]
containers=0
with open('27_A.txt') as f:
    d=f.readlines()
    punkts=d[0]
    
for i in range (1,len(d)):
    data.append(d[i].split())
    
for i in range (0,len(data)):
    position0=int(data[i][0])
    cost=0
    for y in range (0,len(data)):
        containers=round(int(data[y][1])/36)
        if round(int(data[y][1])/36) < int(data[y][1])/36:
            containers=(int(data[y][1])//36) + 1
        cost+=abs(int(data[y][0])-position0) * containers
    cost_punkt.append(cost)    
    print(i, cost)
    
print(f"{min(cost_punkt)} номер пункта-{data[cost_punkt.index(min(cost_punkt))][0]}  всего пунктов {punkts}")

