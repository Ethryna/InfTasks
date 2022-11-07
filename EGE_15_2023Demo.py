for a in range(1,1000):
    Fh = True
    for x in range(1, 10000):
        if ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100):
            Fh = True
        else: 
            Fh = False
            break
    if Fh == True:
        print(a)
        exit()
