def Menu():
    print('Выберите тип решаемой задачи: \n 1 - кодирование текстовой информации \n 2 - кодирование звука \n 3 - кодирование изображения \n Для выхода введите 0 \n')
    type = input('Тип задачи: ')
    if type == '1': InfC()
    elif type == '2': SoC()
    elif type == '3': ImC()
    elif type == '0': exit()
    else:
        print('Недопустимое значение!\n')
        Menu()

def checkInt(a, state):
    try:
        an = int(a)
        state = True
        return state
    except:
        print('Недопустимое значение! Введите число.')
        

def InfC():
    workIn = True
    stInt = False
    findG = False
    while workIn == True:
        formIn = input('Какую формулу используем? \n 1: N = 2^i (N - мощность алфавита, i - разрядность двоичного кода) \n 2: I = k * i (I - информационный объём текста, k - количество символов, i - информационный вес одного символа) \n 0: отмена, вернуться в меню \n')
        if formIn == '1':
            while not findG == True:
                find = input('\nЧто ищем? \n 1 - N (мощность алфавита)\n 2 - i (разрядность двоичного кода)\n ')
                if find == '1' or find == '2':
                    findG = True
                else: print('Недопустимое значение!\n')
            findG = False
            if find == '1':
                while not stInt == True:
                    ih = input(' Введите i (разрядность двоичного кода) в битах: ')
                    stInt = checkInt(ih, stInt)
                i = int(ih)
                stInt = False
                N = 2 ** i
                res = input(f'N (мощность алфавита) = {N} \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
            elif find == '2':
                while not stInt == True:
                    Nh = input(' Введите N (мощность алфавита): ')
                    stInt = checkInt(Nh, stInt)
                N = int(Nh)
                stInt = False
                i = 0
                while not N <= 1:
                    i += 1
                    N = N/2
                if i < 8 or i % 8 != 0:
                    res = input(f'i (разрядность двоичного кода) = {i} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif i >= 8:
                    res = input(f'i (разрядность двоичного кода) = {round(i/8,3)} байт или {i} битов\n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
        elif formIn == '2':
            while not findG == True:
                find = input('\nЧто ищем?\n 1 - I (информационный объём текста)\n 2 - k (количество символов)\n 3 - i (информационный вес одного символа)\n ')
                if find == '1' or find == '2' or find == '3':
                    findG = True
                else:
                    print('Недопустимое значение!\n')
            findG = False
            if find == '1':
                while not stInt == True:
                    kh = input(' Введите k (количество символов): ')
                    stInt = checkInt(kh, stInt)
                k = int(kh)
                stInt = False
                while not stInt == True:
                    ih = input(' Введите i (информационный вес одного символа) в битах: ')
                    stInt = checkInt(ih, stInt)
                i = int(ih)
                stInt = False
                I = k * i
                if I < 8:
                    res = input(f'I (информационный объём текста) = {round(I)} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024:
                    res = input(f'I (информационный объём текста) = {round(I/8, 3)} байт или {round(I)} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024*1024:
                    res = input(f'I (информационный объём текста) = {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {round(I)} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024:
                    res = input(f'I (информационный объём текста) = {round(I/8/1024/1024, 3)} мегабайт или {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {round(I)} битов\n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024*1024:
                    res = input(f'I (информационный объём текста) = {round(I/8/1024/1024/1024, 3)} гигабайт {round(I/8/1024/1024, 3)} мегабайт или {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {round(I)} битов\n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
            elif find == '2':
                while not stInt == True:
                    Ih = input(' Введите I (информационный объём текста) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    ih = input(' Введите i (информационный вес одного символа) в битах: ')
                    stInt = checkInt(ih, stInt)
                i = int(ih)
                stInt = False
                k = I / i
                res = input(f'k (количество символов) = {round(k)} \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
            elif find == '3':
                while not stInt == True:
                    kh = input(' Введите k (количество символов): ')
                    stInt = checkInt(Ih, stInt)
                k = int(kh)
                stInt = False
                while not stInt == True:
                    Ih = input(' Введите I (информационный объём текста) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                i = I / k
                if i < 8 or i % 8 != 0:
                    res = input(f'i (информационный вес одного символа) = {round(i)} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                elif i >= 8:
                    res = input(f'i (информационный вес одного символа) = {round(i/8)} байт или {round(i)} битов \n\nИщем что-то ещё по кодированию текстовой информации? (Y - да, N - нет): ')
                if res == 'N':
                    workIn = False
                    Menu()
        elif formIn == '0':
            workIn = False
            Menu()
        else: print('Недопустимое значение!\n')


def SoC():
    workSo = True
    stInt = False
    findG = False
    while workSo == True:
        formSo = input('Какую формулу используем? \n 1: H = 1/T (H - частота дискретизации, T - шаг дискретизации) \n 2: K = 2^b (K - количество уровней квантования, b - глубина кодирования/разрядность квантования) \n 3: I = RHtb (I - объём звуковой информации, R - количество каналов, H - частота дискретизации, t - время записи, b - глубина кодирования/разрядность квантования) \n 0: отмена, вернуться в меню \n')
        if formSo == '1':
            while not findG == True:
                find = input('\nЧто ищем?\n 1 - H (частоту дискретизации)\n 2 - T (шаг дискретизации)\n ')
                if find == '1' or find == '2':
                    findG = True
                else:
                    print('Недопустимое значение!\n')
            findG = False
            if find == '2':
                while not stInt == True:
                    Hh = input('  Введите H (частоту дискретизации) в Гц: ')
                    stInt = checkInt(Hh, stInt)
                H = int(Hh)
                stInt = False
                T = 1 / H
                res = input(f'T (шаг дискретизации) = {round(T, 3)} с \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == '1':
                while not stInt == True:
                    Th = input(' Введите T (шаг дискретизации) в секундах: ')
                    stInt = checkInt(Th, stInt)
                T = int(Th)
                stInt = False
                H = 1 / T
                if H < 1000:
                    res = input(f'H (частота дискретизации) = {round(H, 3)} Гц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif H >= 1000:
                    res = input(f'H (частота дискретизации) = {round(H/1000, 3)} кГц или {round(H, 3)} Гц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
        elif formSo == '2':
            while not findG == True:
                find = input('\nЧто ищем?\n 1 - K (количество уровней квантования)\n 2 - b (глубину кодирования/разрядность квантования)\n ')
                if find == '1' or find == '2':
                    findG = True
                else:
                    print('Недопустимое значение!\n')
            findG = False
            if find == '1':
                while not stInt == True:
                    bh = input(' Введите b (глубину кодирования/разрядность квантования) в битах: ')
                    stInt = checkInt(bh, stInt)
                b = int(bh)
                stInt = False
                K = 2 ** b
                res = input(f'K (количество уровней квантования) = {K} \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == '2':
                while not stInt == True:
                    Kh = input(' Введите K (количество уровней квантования): ')
                    stInt = checkInt(Kh, stInt)
                K = int(Kh)
                stInt = False
                b = 0
                while not K <= 1:
                    b += 1
                    K = K/2
                res = input(f'b (глубина кодирования/разрядность квантования) = {b} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
        elif formSo == '3':
            while not findG == True:
                find = input('\nЧто ищем?\n 1 - I (объём звуковой информации)\n 2 - R (количество каналов)\n 3 - H (частоту дискретизации)\n 4 - t (время записи)\n 5 - b (глубину кодирования/разрядность квантования)\n ')
                if find == '1' or find == '2' or find == '3' or find == '4' or find == '5':
                    findG = True
                else:
                    print('Недопустимое значение!\n')
            findG = False
            if find == '1':
                while not stInt == True:
                    Rh = input(' Введите R (количество каналов): ')
                    stInt = checkInt(Rh, stInt)
                R = int(Rh)
                stInt = False
                while not stInt == True:
                    Hh = input(' Введите H (частоту дискретизации) в Гц: ')
                    stInt = checkInt(Hh, stInt)
                H = int(Hh)
                stInt = False
                while not stInt == True:
                    th = input(' Введите t (время записи) в секундах: ')
                    stInt = checkInt(th, stInt)
                t = int(th)
                stInt = False
                while not stInt == True:
                    bh = input(' Введите b (глубину кодирования/разрядность квантования) в битах: ')
                    stInt = checkInt(bh, stInt)
                b = int(bh)
                stInt = False
                I = R * H * t * b
                if I < 8:
                    res = input(f'I (объём звуковой информации) = {I} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024:
                    res = input(f'I (объём звуковой информации) = {round(I/8, 3)} байт или {I} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024*1024:
                    res = input(f'I (объём звуковой информации) = {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {I} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024:
                    res = input(f'I (объём звуковой информации) = {round(I/8/1024/1024, 3)} мегабайт или {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {I} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024*1024:
                    res = input(f'I (объём звуковой информации) = {round(I/8/1024/1024/1024, 3)} гигабайт или {round(I/8/1024/1024, 3)} мегабайт или {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {I} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif res == 'N':
                    workSo = False
                    Menu()
            elif find == '2':
                while not stInt == True:
                    Ih = input(' Введите I (объём звуковой информации) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    Hh = input(' Введите H (частоту дискретизации) в Гц: ')
                    stInt = checkInt(Hh, stInt)
                H = int(Hh)
                stInt = False
                while not stInt == True:
                    th = input(' Введите t (время записи) в секундах: ')
                    stInt = checkInt(th, stInt)
                t = int(th)
                stInt = False
                while not stInt == True:
                    bh = input(' Введите b (глубину кодирования/разрядность квантования) в битах: ')
                    stInt = checkInt(bh, stInt)
                b = int(bh)
                stInt = False
                R = I / (H * t * b)
                res = input(f'R (количество каналов) = {round(R)} \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == '3':
                while not stInt == True:
                    Ih = input(' Введите I (объём звуковой информации) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    Rh = input(' Введите R (количество каналов): ')
                    stInt = checkInt(Rh, stInt)
                R = int(Rh)
                stInt = False
                while not stInt == True:
                    th = input(' Введите t (время записи) в секундах: ')
                    stInt = checkInt(th, stInt)
                t = int(th)
                stInt = False
                while not stInt == True:
                    bh = input(' Введите b (глубину кодирования/разрядность квантования) в битах: ')
                    stInt = checkInt(bh, stInt)
                b = int(bh)
                stInt = False
                H = I / (R * t * b)
                if H < 1000:
                    res = input(f'H (частота дискретизации) = {round(H, 3)} Гц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif H >= 1000:
                    res = input(f'H (частота дискретизации) = {round(H/1000, 3)} кГц или {round(H, 3)} Гц\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == '4':
                while not stInt == True:
                    Ih = input(' Введите I (объём звуковой информации) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    Rh = input(' Введите R (количество каналов): ')
                    stInt = checkInt(Rh, stInt)
                R = int(Rh)
                stInt = False
                while not stInt == True:
                    Hh = input(' Введите H (частоту дискретизации) в Гц: ')
                    stInt = checkInt(Hh, stInt)
                H = int(Hh)
                stInt = False
                while not stInt == True:
                    bh = input(' Введите b (глубину кодирования/разрядность квантования) в битах: ')
                    stInt = checkInt(bh, stInt)
                b = int(bh)
                stInt = False
                t = I / (R * H * b)
                if t < 60:
                    res = input(f't (время записи) = {round(t)} секунд \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif t < 3600:
                    res = input(f't (время записи) = {round(t//60)}:{round(t%60)} минут или {round(t)} секунд\n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                elif t >= 3600:
                    res = input(f't (время записи) = {round(t//3600)}:{round((t%3600)//60)}:{round((t%3600)%60)} часов или {round(t//60)}:{round(t%60)} минут или {round(t)} секунд \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == '5':
                while not stInt == True:
                    Ih = input(' Введите I (объём звуковой информации) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    Rh = input(' Введите R (количество каналов): ')
                    stInt = checkInt(Rh, stInt)
                R = int(Rh)
                stInt = False
                while not stInt == True:
                    Hh = input(' Введите H (частоту дискретизации) в Гц: ')
                    stInt = checkInt(Hh, stInt)
                H = int(Hh)
                stInt = False
                while not stInt == True:
                    th = input(' Введите t (время записи) в секундах: ')
                    stInt = checkInt(th, stInt)
                t = int(th)
                stInt = False
                b = I / (R * H * t)
                res = input(f'b (глубина кодирования/разрядность квантования) = {round(b)} битов \n\nИщем что-то ещё по кодированию звука? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
        elif formSo == '0':
            workSo = False
            Menu()
        else: print('Недопустимое значение!\n')


def ImC():
    workIm = True
    stInt = False
    findG = False
    while workIm == True:
        formIm = input('Какую формулу используем? \n 1: N = 2^i (N - количество цветов, i - разрядность двоичного кода/битовая глубина) \n 2: I = h * s (I - информационный объём изображения, h - высота изображения в пикселях, s - ширина изображения в пикселях, i - разрядность двоичного кода/битовая глубина) \n0: отмена, вернуться в меню \n')
        if formIm == '1':
            while not findG == True:
                find = input('\nЧто ищем?\n 1- N (количество цветов)\n 2 - i (разрядность двоичного кода)\n ')
                if find == '1' or find == '2':
                    findG = True
                else:
                    print('Недопустимое значение!\n')
            findG = False
            if find == '1':
                while not stInt == True:
                    ih = input(' Введите i (разрядность двоичного кода) в битах: ')
                    stInt = checkInt(ih, stInt)
                i = int(ih)
                stInt = False
                N = 2 ** i
                res = input(f'N (количество цветов) = {N} \n\nИщем что-то ещё по кодированию изображений? (Y - да, N - нет)')
                if res == 'N':
                    workIm = False
                    Menu()
            elif find == '2':
                while not stInt == True:
                    Nh = input(' Введите N (количество цветов): ')
                    stInt = checkInt(Nh, stInt)
                N = int(Nh)
                stInt = False
                i = 0
                while not N <= 1:
                    i += 1
                    N = N/2
                if i < 8 or i % 8 != 0:
                    res = input(f'i (разрядность двоичного кода) = {i} битов \n\nИщем что-то ещё по кодированию изображений? (Y - да, N - нет)')
                if i >= 8:
                    res = input(f'i (разрядность двоичного кода) = {round(i/8)} байт или {i} битов \n\nИщем что-то ещё по кодированию изображений? (Y - да, N - нет)')
                if res == 'N':
                    workIm = False
                    Menu()
        elif formIm == '2':
            while not findG == True:
                find = input('\nЧто ищем?\n 1 - I (информационный вес изображения)\n 2 - h (высоту изображения в пикселях)\n 3 - s (ширину изображения)\n 4 - i (разрядность двоичного кода/битовая глубина)\n ')
                if find == '1' or find == '2' or find == '3' or find == '4':
                    findG = True
                else:
                    print('Недопустимое значение!\n')
            findG = False
            
            if find == '1':
                while not stInt == True:
                    ih = input(' Введите i (разрядность двоичного кода/глубину кодирования) в битах: ')
                    stInt = checkInt(ih, stInt)
                i = int(ih)
                stInt = False
                while not stInt == True:
                    hh = input(' Введите h (высоту изображения в пикселях): ')
                    stInt = checkInt(hh, stInt)
                h = int(hh)
                stInt = False
                while not stInt == True:
                    sh = input(' Введите s (ширину изображения в пикселях): ')
                    stInt = checkInt(sh, stInt)
                s = int(sh)
                stInt = False
                I = h * s * i
                if I < 8:
                    res = input(f'I (информационный вес изображения) = {I} битов \n\nИщем что-то ещё по кодированию изображения? (Y - да, N - нет): ')
                elif I < 8*1024:
                    res = input(f'I (информационный вес изображения) = {round(I/8, 3)} байт или {I} битов \n\nИщем что-то ещё по кодированию изображения? (Y - да, N - нет): ')
                elif I < 8*1024*1024:
                    res = input(f'I (информационный вес изображения) = {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {I} битов\n\nИщем что-то ещё по кодированию изображения? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024:
                    res = input(f'I (информационный вес изображения) = {round(I/8/1024/1024, 3)} мегабайт или {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {I} битов \n\nИщем что-то ещё по кодированию изображения? (Y - да, N - нет): ')
                elif I < 8*1024*1024*1024*1024:
                    res = input(f'I (информационный вес изображения) = {round(I/8/1024/1024/1024, 3)} гигабайт или {round(I/8/1024/1024, 3)} мегабайт или {round(I/8/1024, 3)} килобайт или {round(I/8, 3)} байт или {I} битов \n\nИщем что-то ещё по кодированию изображения? (Y - да, N - нет): ')
                elif res == 'N':
                    workSo = False
                    Menu()
            elif find == '2':
                while not stInt == True:
                    Ih = input(' Введите I (информационный вес изображения) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    sh = input(' Введите s (ширину изображения в пикселях): ')
                    stInt = checkInt(sh, stInt)
                s = int(sh)
                stInt = False
                while not stInt == True:
                    ih = input(' Введите i (разрядность двоичного кода/глубину кодирования) в битах: ')
                    stInt = checkInt(ih, stInt)
                i = int(ih)
                stInt = False
                i = I / (i * s)
                res = input(f'h (высота изображения в пикселях) = {round(h)} \n\nИщем что-то ещё по кодированию изображения ? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == '3':
                while not stInt == True:
                    Ih = input(' Введите I (информационный вес изображения) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    hh = input(' Введите h (высоту изображения в пикселях): ')
                    stInt = checkInt(hh, stInt)
                h = int(hh)
                stInt = False
                while not stInt == True:
                    ih = input(' Введите i (разрядность двоичного кода/глубину кодирования) в битах: ')
                    stInt = checkInt(ih, stInt)
                i = int(ih)
                stInt = False
                i = I / (i * h)
                res = input(f's (ширина изображения в пикселях) = {round(s)} \n\nИщем что-то ещё по кодированию изображения ? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
            elif find == '4':
                while not stInt == True:
                    Ih = input(' Введите I (информационный вес изображения) в битах: ')
                    stInt = checkInt(Ih, stInt)
                I = int(Ih)
                stInt = False
                while not stInt == True:
                    sh = input(' Введите s (ширину изображения в пикселях): ')
                    stInt = checkInt(sh, stInt)
                s = int(sh)
                stInt = False
                while not stInt == True:
                    hh = input(' Введите h (ширину изображения в пикселях): ')
                    stInt = checkInt(hh, stInt)
                h = int(hh)
                stInt = False
                i = I / (h * s)
                res = input(f'i (разрядность двоичного кода/глубину кодирования) = {round(i)} \n\nИщем что-то ещё по кодированию изображения ? (Y - да, N - нет): ')
                if res == 'N':
                    workSo = False
                    Menu()
        elif formIm == '0':
            workIm = False
            Menu()
        else: print('Недопустимое значение!\n')
Menu()
