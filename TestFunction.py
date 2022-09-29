#Тестовая функция
work = True
a = float(0)
b = float(0)
c = float(0)
act = ''

def summ(a,b):
    c = a+b
    return c
def subst(a,b):
    c = a-b
    return c
def mult(a,b):
    c = a*b
    return c
def divide(a,b):
    c = a/b
    return c
def expon(a,b):
    c = a**b
    return c

while work == True:
    data = input('Введите пример. Для выхода введите 0: ')
    if data != '0':
        st = data.split()
        a = int(st[0])
        b = int(st[2])
        if st[1] == '+':
            print(f'Ответ = {summ(a,b)}')
        if st[1] == '-':
            print(f'Ответ = {subst(a,b)}')
        if st[1] == '*':
            print(f'Ответ = {mult(a,b)}')
        if st[1] == '/':
            print(f'Ответ = {divide(a,b)}')
        if st[1] == '**':
            print(f'Ответ = {expon(a,b)}')
    else:
        work = False
    
