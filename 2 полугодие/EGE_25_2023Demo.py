def f(c):
    if int(c)%2023==0:
        ost=int(c)//2023
        res.append(c)
        resost.append(ost)

res=[]
resost=[]
for i in range(10):
  for y in range(1000000):
      c='1'+str(i)+'21394'
      f(c)

      c='1'+str(i)+'2139'+str(y)+'4'
      if int(c)>10**10: break
      f(c)
      
for i in res: print(i)
print('\n')
for i in resost: print(i)
