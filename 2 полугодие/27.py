with open('27-A.txt') as f:
    conts = int(f.readline())
    trash = []
    for i in range(conts):
        trash.append(int(f.readline()))

mid = conts//2

roads = trash
roads.extend(trash)
prices = []
Ps = []
for i in range(conts):
    d = roads[i:i+conts]
    price = 0
    pricef = 1000000
    P = mid+i+1
    while not P<=conts:
        P-=conts
    for k in range(mid):
        price+=(d[mid-k]*k+d[mid+k]*k)
    prices.append(price)
    Ps.append(P)
print(min(prices),Ps[prices.index(min(prices))])

##Not finished, wrong answer
