#? - 1 symbol
#* - any amount of symbols
#1?2139*4 mod 2023 == 0
for i in range(2023,10**10, 2023):
    s = str(i)
    if s[0]=='1' and s[2] == '2' and s[3] == '1' and s[4] == '3' and s[5] == '9' and s[-1] == '4':
        print(s,i//2023)
