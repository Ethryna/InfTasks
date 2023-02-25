with open('27-A.txt') as f:
    conts = [int(x) for x in f]
    conts.pop(0)
    trash = []

mid = len(conts)//2
leng = len(conts)
conts = conts+conts
prices = []
for i in range(leng):
    d = conts[i:i+leng]
    print(d)
    price = 0
    pricef = 1000000
    P = mid+i+1
    index = 0
    for k in range(len(d)):
        if k<mid:
        	index = k
        else:
        	index = leng-k
        price += d[k]*index
    prices.append(price)
print(prices)
print(prices.index(min(prices))+1)
