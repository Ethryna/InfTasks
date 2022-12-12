a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
""" Метод проще, но увы.
a = (f'{a} {b} {c}')
b = list(map(int,a.split()))
b = sorted(b)
a = b[0]
c = b[2]
b = b[1]
print(f'a = {a}\nb = {b}\nc = {c}')"""

while not (a<=b and b<=c): 
    if b<a:
        a = b+a
        b = a-b
        a = a-b
    if c<a:
        a = c+a
        c = a-c
        a = a-c
    if c<b:
        b = c+b
        c = b-c
        b = b-c
print(f'a = {a}\nb = {b}\nc = {c}')
