def Menu():
    print('Выберите тип решаемой задачи: \n 1 - кодирование текстовой информации \n 2 - кодирование звука \n 3 - кодирование изображения \n Для выхода введите 0 \n')
    type = input('Тип задачи: ')
    if type == '1': InfC()
    if type == '2': SoC()
    if type == '3': ImC()
    if type == '0': exit()

def InfC():
    workIn = True
    while workIn == True:
        find = input('Что известно? По завершении введите 0: \n N - мощность алфавита \n i - разрядность двоичного кода (или информационный вес символа в битах) \n k = количество символов в тексте \n I - информационный объём текста')
        known = []
        Numbers = []
        l = ''
        while not l == '0':
            l = input('Что известно? По завершении введите 0: \n N - мощность алфавита \n i - разрядность двоичного кода (или информационный вес символа в битах) \n k = количество символов в тексте \n I - информационный объём текста')
            if l != '0':
                known.append(l)
        print('Введите числовые значения известных величин (объёмы - в битах): ')
        for o in range(len(known)):
            num = int(input(f'known[o] = '))
            Numbers.append(num)
        """formIn = input('Какую формулу используем? \n 1: N = 2^i (N - мощность алфавита, i - разрядность двоичного кода) \n 2: I = k * i (I - информационный объём текста) \n 0: отмена, вернуться в меню \n')
        if formIn == '1':
            find = input('Что ищем: N или i?: ')
            if find == 'N':
                i = int(input('Введите i: '))
                N = 2 ** i
                res = input(f'N = {N} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workIn = False
            elif find == 'i':
                N = int(input('Введите N: '))
                i = 0
                while not N < 2:
                    i += 1
                    N = N//2
                res = input(f'i = {i} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workIn = False
        elif formIn == '2':
            find = input('Что ищем: I, k или i?: ')
            if find == 'I':
                k = int(input('Введите k: '))
                i = int(input('Введите i: '))
                I = k * i
                res = input(f'I = {I} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workIn = False
            elif find == 'k':
                I = int(input('Введите I: '))
                i = int(input('Введите i: '))
                k = I // i
                res = input(f'k = {k} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workIn = False
            elif find == 'i':
                k = int(input('Введите k: '))
                I = int(input('Введите I: '))
                i = I // k
                res = input(f'i = {i} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workIn = False
        elif formIn == '0':
            workIn = False
            Menu()"""


def SoC():
    workSo = True
    while workSo == True:
        formSo = input('Какую формулу используем? \n 1: H = 1/T \n 2: K = 2^b \n 3: I = Htb \n 0: отмена, вернуться в меню')
        if formSo == '1':
            find = input('Что ищем: H или T?: ')
            if find == 'H':
                H = input('Введите H: ')
                T = 1 // H
                res = input(f'T = {T} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False
            elif find == 'T':
                H = input('Введите T: ')
                H = 1 // T
                res = input(f'H = {H} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False
        elif formSo == '2':
            find = input('Что ищем: K или b?: ')
            if find == 'K':
                b = int(input('Введите b: '))
                K = 2 ** b
                res = input(f'K = {K} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False
            elif find == 'b':
                K = int(input('Введите K: '))
                b = 0
                while not K < 2:
                    b += 1
                    K = K//2
                res = input(f'b = {b} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False 
        elif formSo == '3':
            find = input('Что ищем: I, H, t или b?: ')
            if find == 'I':
                H = int(input('Введите H: '))
                t = int(input('Введите t: '))
                b = int(input('Введите b: '))
                I = H * t * b
                res = input(f'I = {I} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False
            elif find == 'H':
                I = int(input('Введите I: '))
                t = int(input('Введите t: '))
                b = int(input('Введите b: '))
                H = I // (t * b)
                res = input(f'H = {H} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False
            elif find == 't':
                b = int(input('Введите b: '))
                I = int(input('Введите I: '))
                H = int(input('Введите H: '))
                t = I // (H * b)
                res = input(f't = {t} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False
            elif find == 'b':
                t = int(input('Введите t: '))
                I = int(input('Введите I: '))
                H = int(input('Введите H: '))
                b = I // (H * t)
                res = input(f'b = {b} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workSo = False
        elif formSo == '0':
            workSo = False
            Menu()


def ImC():
    workIm = True
    while workIm == True:
        formIm = input('Какую формулу используем? \n 1: N = 2^i \n 0: отмена, вернуться в меню')
        if formIm == '1':
            find = input('Что ищем: N или i?: ')
            if find == 'N':
                i = int(input('Введите i: '))
                N = 2 ** i
                res = input(f'N = {N} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workIm = False
            elif find == 'i':
                N = int(input('Введите N: '))
                i = 0
                while not N < 2:
                    i += 1
                    N = N//2
                res = input(f'i = {i} \n Ищем что-то ещё? (Y - да, N - нет)')
                if res == 'N':
                    workIm = False
        elif formIm == '0':
            workIm = False
            Menu()