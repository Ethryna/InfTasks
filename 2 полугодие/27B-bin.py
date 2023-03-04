with open('27-B.txt') as f:
    conts = [int(x) for x in f]
    conts.pop(0)
    trash = []

leng = len(conts)
M = leng//2
conts = conts+conts
start = 0
end = leng
while True:
    mid = (end-start)//2
    if mid == 0:
        mid = 1
    if end-start == 0:
        mid = 0
    print(f'Старт в {start}, конец в {end}, проверяем {start+mid}  и {start+mid+1}')
    
    prices = []
    price = 0

    d = conts[mid:mid+leng]
    for k in range(len(d)):
        if k<M: index = k
        else: index = leng-k
        price += d[k]*index
    prices.append(price)
    
    price = 0
    d = conts[mid+1:mid+1+leng]
    for k in range(len(d)):
        if k<M: index = k
        else: index = leng-k
        price += d[k]*index
    prices.append(price)
        
    print(prices)
    if prices[0]>prices[1]:
        print(f'{start+mid+1} {prices[1]}')
        start += mid
    else:
        print(f'{start+mid} {prices[0]}')
        end -= mid
       

    input()
        
