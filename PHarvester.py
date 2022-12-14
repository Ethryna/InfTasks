def p1():
    N10 = int(input('Введите исходное 10-тичное число: '))
    p = 1
    while ((p<2) or (p>9)):
        p = int(input('Введите основание системы счисления в диапазоне [2; 9]: '))
    k = int(1)
    Np = int(0)
    while not (N10 == 0):
        Np = Np + (N10 % p)*k
        k = k*10
        N10 = N10 // p
    print('N' + str(p) + ' = ' + str(Np)+'\n')
    input()
    Menu()

    
def p2():
    p = int(input('Введите основание СС исходного числа: p = '))
    Np = int(input(f'Введите исходное число: N{p} = '))
    k = int(1)
    N10 = int(0)
    while not Np == 0:
        N10 = N10+(Np%10)*k
        k = k*p
        Np = Np//10
    print(f'N10 = {N10}\n')
    input()
    Menu()

    
def p3():
    s = 0
    while not s in [k for k in range(3,11)]:
        s = int(input('Введите основание p (2 < p <= 10): '))
    print(f'\nТаблица умножения для {s}-ричной СС')
    for i in range(1,s):
        for j in range(1,s):
            x = (i*j//s)*10+(i*j%s)
            if x < 10:
                print(f'    {x}',end=' ')
            elif x >= 10 and x < 100:
                print(f'  {x}',end=' ')
        print('')
    print('\n')
    input()
    Menu()

    
def p4():
    A = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    a = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')  
    Morze = list([".-","-...",".--","--.","-..",".","...-","--..","..",".---","-.-",".-..","--","-.","---",".--.",".-.","...","-","..-","..-.","....","-.-.","---.","----","--.-",".--.-","-.--","-..-","..-..","..--",".-.-"])
    InpS = input('Введите исходную строку: ')
    OutS = str('')
    for i in range(1, (len(InpS)+1)):
        for j in range (1, 32):
            if (InpS[i-1] == str(A[j-1])) or (InpS[i-1] == str(a[j-1])):
                OutS = OutS + str(Morze[j-1]) + ' '
        if InpS[i-1]==' ':
            OutS = OutS + '   '
    print('\nВаша строка, перекодированная на азбуку Морзе: ' +OutS+'\n')
    input()
    Menu()
    

def p5():
    Tabl = [[n for n in range(0,10)], ['0000000','0001111','0010110','0011001','0100101','0101010','0110011','0111100','1000011','1001100']]
    Code = ''
    
    def Distance(A, B):
        K = int(7)
        for i in range(1,8):
            if (int(A)%10) == (int(B)%10):
                K = K-1
            A = A[0:len(A)-1]
            B = B[0:len(B)-1]
        return(K)
    
    while not len(Code) == 7:
        Code = input('Код = ')

    minD = Distance(Code, Tabl[1][0])
    Num = 0
    for j in range(1,10):
        D = Distance(Code, Tabl[1][j])
        if D<minD:
            minD = D
            Num = j
    if minD == 0:
        print(f'Код верный: символ {Tabl[0][Num]}\n')
    elif minD == 1:
        print(f'Код исправлен: символ {Tabl[0][Num]}\n')    
    else: print('Код неверный.\n')
    input()
    Menu()
    

def Menu():
    t = input('Какую программу вы хотите запустить?\n1 - перевод из десятичной СС в указанную\n2 - перевод из указанной СС в десятичную\n3 - таблица умножения для СС с основанием p (2 < p <= 10)\n4 - кодирование строки азбукой Морзе\n5 - алгоритм Хемминга\n\n')
    if t == '1':
        p1()
    elif t == '2':
        p2()
    elif t == '3':
        p3()
    elif t == '4':
        p4()
    elif t == '5':
        p5()

Menu()
