from itertools import *
def repl(a):
    if a == '01': return 712
    elif a == '02': return 673
    elif a == '03': return 1075
    elif a == '04': return 875
    elif a == '05': return 1622
    elif a == '06': return 423
    elif a == '10': return 712
    elif a == '12': return 1385
    elif a == '13': return 1800
    elif a == '14': return 1577
    elif a == '15': return 2348
    elif a == '16': return 1128
    elif a == '20': return 673
    elif a == '21': return 1385
    elif a == '23': return 1499
    elif a == '24': return 239
    elif a == '25': return 2046
    elif a == '26': return 244
    elif a == '30': return 1075
    elif a == '31': return 1800
    elif a == '32': return 1499
    elif a == '34': return 1287
    elif a == '35': return 551
    elif a == '36': return 1266
    elif a == '40': return 875
    elif a == '41': return 1577
    elif a == '42': return 239
    elif a == '43': return 1287
    elif a == '45': return 1835
    elif a == '46': return 442
    elif a == '50': return 1622
    elif a == '51': return 2348
    elif a == '52': return 2046
    elif a == '53': return 551
    elif a == '54': return 1835
    elif a == '56': return 1813
    elif a == '60': return 423
    elif a == '61': return 1128
    elif a == '62': return 244
    elif a == '63': return 1266
    elif a == '64': return 442
    elif a == '65': return 1813
    elif a == '00': return 0
    elif a == '11': return 0
    elif a == '22': return 0
    elif a == '33': return 0
    elif a == '44': return 0
    elif a == '55': return 0
    elif a == '66': return 0

def city(s):
    if s == '0': return 'Москва     '
    if s == '1': return 'Санкт-Петербург     '
    if s == '2': return 'Чебоксары     '
    if s == '3': return 'Ростов-на-Дону     '
    if s == '4': return 'Ульяновск     '
    if s == '5': return 'Сочи     '
    if s == '6': return 'Нижний Новгород     '
    
ways = list(product('0123456',repeat=7))
waysR = []
wR = []
waysL = 0
n = 0
for k in ways:
    l = ''.join(k)
    if l.count('0')==1 and l.count('1')==1 and l.count('2')==1 and l.count('3')==1 and l.count('4')==1 and l.count('5')==1 and l.count('6')==1:        
        c = 0
        for j in range(6):
            s = l[j:j+2]
            c+= repl(s)
        if c > waysL:
            waysR = []
            waysR.append(l)
            waysL = c
        elif c == waysL:
            waysR.append(l)
for p in waysR:
    Y = ''
    for t in p:
        Y += city(t)
    wR.append(Y)
print(waysL)
print(wR)
