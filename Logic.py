print('Значение логического выражения ((A & не B)->C)<-> равно нулю при:')
for a in range(2):
    for b in range(2):
        for c in range(2):
            F = (((a and not(b))<=c)==a)
            if F == False:
                print (f'a = {a}, b = {b}, c = {c}')
