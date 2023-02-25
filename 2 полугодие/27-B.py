with open('27-B.txt') as f:
    conts = [int(x) for x in f]
    conts.pop(0)
    trash = []

mid = len(conts)//2
leng = len(conts)
conts = conts+conts
prices = []
step = 500000
start = 0
while step >= 1:
    prices = []
    step //= 10
    if step == 0: step = 1
    print(f'Круг: начало в пункте {start}, шаг {step}, конец в {start+step*20}\n')
    for i in range(20):
        d = conts[start+i*step:start+i*step+leng]
        price = 0
        index = 0
        for k in range(len(d)):
            if k<mid: index = k
            else: index = leng-k
            price += d[k]*index
        prices.append(price)
    print(prices.index(min(prices))*step+start+1)
    start = start+prices.index(min(prices))*step-step
