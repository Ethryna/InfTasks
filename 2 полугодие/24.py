flag = 0
c = 0
cm = 0
with open('24.txt') as f:
    s = f.readline()
    s = s.replace('O','A')
    s = s.replace('C','D')
    s = s.replace('F','D')
    s = s.replace('AD','*')
    for i in s:
        if i == '*':
            c+=1
            if c > cm: cm = c
        else:
            c = 0
    print(cm)
