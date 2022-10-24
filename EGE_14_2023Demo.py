# 123x5 + 1x233 значение должно быть кратно 14
a = '123x5'
b = '1x233'
Found = False;
for x in range(0,15):
    a10 = 1*15**4+2*15**3+3*15**2+x*15+5;
    b10 = 1*15**4+x*15**3+2*15**2+3*15+3;
    if (a10+b10)%14 == 0 and Found == False:
        A = x;
        Found = True;
        Sum = a10+b10
print(A,Sum//14);        