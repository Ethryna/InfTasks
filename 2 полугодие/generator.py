#a = [1,2,3]
#b = [i*2 for i in a if i<3]
#b = [[i,f] for i,f in enumerate(a)]
#a2 = [10,20,30]
"""b = [i+j for i,j in zip(a,a2)]
print(b)"""
'''i=1
print('1') if i==1 else _'''
#b = [("true" if n>2 else "false") for n in a]
#b2 = [i+j for i in a for j in a2]
'''b = [[i for i in range(1,n+1)] for n in a]
print(b)'''
#print(b2)
'''">=5"
x = [[name,'+st' if sum(score)/len(score)==5 else "-"] for name,gender,score in st]
print(x)'''

'''from itertools import *

st = []
st2 = ['b','f',[5,5,5]]
st3 = ['c','m',[2,1,2]]

a = st+st2+st3
print(a)
a = [*st,*st2,*st3]
print(a)
a = list(chain(st,st2,st3))
print(a)
s = [st,st2,st3]
a = list(chain(n for n in s))
print(a)'''

'''def f(x):
    return x*x

f2 = lambda y,x: x*y
print(f2(5,3))'''

"""a = "0"

f3 = lambda x: 1 if all(x) else 0
print(f3(a))"""

#a = [1,2,3]
#b = list(map(lambda x: str(x**2)+'a',a))
#print(b)

c ='12345'
b = list(filter(lambda x: int(x)%2==0,c))
print(b)
