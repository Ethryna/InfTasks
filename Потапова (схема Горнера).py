n = int(input('Введите основание системы счисления: '))
x = str(input('Введите число для перевода в десятичную систему счисления: '))
k = len(x)
result = 0

for i in range(1, k):
    result = result + int(x[i]) * n
    if i < k-1:
        result = result + int(x[i+1])
    print(result)
print('Число ' + x + ' в десятичной системе счисления = ' + str(result))

#пока не работает
