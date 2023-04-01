# Задание 1
![Снимок экрана 2023-04-01 105900](https://user-images.githubusercontent.com/114387952/229264815-842f7c32-b419-4f53-892a-436017768c6b.png)  
_Надо определённо научиться нормально считать_ -_-  
**Ответ: 22** (верно)  
  
# Задание 2

for x in range(2):  
    for y in range(2):  
        for z in range(2):  
            for w in range(2):  
                F = (x and (not(y) and z and w or y and not(w)))  
                if F == 1:  
                    print(x,y,z,w)  
                      
**Ответ: y w z x** (верно)
  
# Задание 3
**Ответ: 37199** (верно)
  
# Задание 4
**Ответ: 161116** (верно)
# Задание 5
c=0  
for i in range(10000):  
    N = i  
      
    if N%3==0:  
        N//=3  
    else:  
        N-=1  
          
    if N%5==0:  
        N//=5  
    else:  
        N-=1  
  
    if N%11==0:  
        N//=11  
    else:  
        N-=1  
  
    if N==8: c+=1  
print(c)  
**Ответ: 4** (верно)
  
# Задание 6  
from turtle import *  
for i in range(10):  
    right(60)  
    forward(10*30)  
    right(60)  
penup()  
for x in range(-5,6):  
    for y in range(-10,1):  
        goto(x*30,y*30)  
        dot(3)  
**Ответ: 42** (верно)  
  
# Задание 7
**Ответ: 20** (верно)  

# Задание 8
from itertools import product  
c=0  
for x in range(2,7):  
    a = list(product('еия', repeat=x))  
    for k in a:  
        s = ''.join(k)  
        if (s.count('е')<=2 and s.count('и')<=2 and s.count('я')<=2):  
            c+=1  
    print(c)  
print(3*c-9)  
  
**Ответ: 792** (верно)  

# Задание 9
**Ответ: 1549** (верно)  

# Задание 10
**Ответ: 22** (верно)  

# Задание 11
**Ответ: 76** (верно)  
