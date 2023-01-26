for x in '012345678abcde':
    if (int(f'123{x}5',15)+int(f'1{x}233',15))%14==0:
        print(x, (int('123'+x+'5',15) + int('1'+x+'233',15))//14)
        break
