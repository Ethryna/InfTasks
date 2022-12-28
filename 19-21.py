a = 17

print('19 задание:')
print(f'{(223-17)/4} - округлить в бОльшую сторону\n')

print('20 задание:')
for s  in range(102,0,-1):
    if (a+1)+1+s < 223 and 2*(a+1)+s < 223 and (a+1)+s+1 < 223 and (a+1)+2*s < 223:
        if (a+1)+1+s*2 >= 223 and 2*(a+1)+s*2 >= 223 and (a+1)+(s+1)*2 >= 223 and (a+1)+2*s*2 >= 223:
            print(s)
    if (2*a)+1+s < 223 and 2*(2*a)+s < 223 and (2*a)+s+1 < 223 and (2*a)+2*s < 223:
        if (2*a)+1+s*2 >= 223 and 2*(2*a)+s*2 >= 223 and (2*a)+(s+1)*2 >= 223 and (2*a)+2*s*2 >= 223:
            print(s)
    if a+1+(s+1) < 223 and 2*a+(s+1) < 223 and a+(s+1)+1 < 223 and a+2*(s+1) < 223:
        if a+1+(s+1)*2 >= 223 and 2*a+(s+1)*2 >= 223 and a+((s+1)+1)*2 >= 223 and a+2*(s+1)*2 >= 223:
            print(s)
    if a+1+s*2 < 223 and 2*a+(s*2) < 223 and a+(s*2)+1 < 223 and a+2*(s*2) < 223:
        if a+1+(s*2)*2 >= 223 and 2*a+(s*2)*2 >= 223 and a+((s*2)+1)*2 >= 223 and a+2*(s*2)*2 >= 223:
            print(s)

sl = []
sl2 = []
for s in range(1,206):
    if  (a+1)+s*2 < 223 and (a+s*2*2*2*2 >= 223 or a*2*2*2*2+s >= 223):          #исключаем 100% победу на 2 ходу (1й ход Вани) и партии, требующие больше 4 ходов
        sl.append(s)

def c(x,y,h):
    if (h == 3 or h == 5) and x+y >= 223:
        return 1
    elif h == 5 and x+y < 223:
        return 0
    elif x+y >= 223 and h<5:
        return 0
    else:
        if h%2 == 0:
            return (c(x+1,y,h+1) or c(x,y+1,h+1) or c(x*2,y,h+1) or c(x,y*2,h+1))
        else:
            return (c(x+1,y,h+1) and c(x,y+1,h+1) and c(x*2,y,h+1) and c(x,y*2,h+1))

print('\nЗадание 21:')
for n in range(1,206):
    if  c(n,17,1)==1:
        sl2.append(n)
print(sl2)

