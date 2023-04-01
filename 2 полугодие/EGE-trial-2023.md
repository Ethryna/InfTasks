# Задание 1
![Снимок экрана 2023-04-01 105900](https://user-images.githubusercontent.com/114387952/229264815-842f7c32-b419-4f53-892a-436017768c6b.png)  
_Надо определённо научиться нормально считать_ -_-  
**Ответ: 22**  
  
# Задание 2

for x in range(2):  
    for y in range(2):  
        for z in range(2):  
            for w in range(2):  
                F = (x and (not(y) and z and w or y and not(w)))  
                if F == 1:  
                    print(x,y,z,w)  
                      
**Ответ: y w z x**
  
# Задание 3
**Ответ: 30633***  
  
# Задание 4
**Ответ: 614142**
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
**Ответ: 4**
  
# Задание 6
