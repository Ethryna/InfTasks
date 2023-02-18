from functools import *

def nums(n):
    for i in range(n):
        yield i
        
b = reduce(lambda x,y: x+y, nums(10))
print(b)
