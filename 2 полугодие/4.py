"12->489"
"-1"
"*7"
from itertools import *
for i in range(1,6):
    b = product("12",repeat=i)
    for j in b:
        prog = "".join(j)
        c = 12
        for k in prog:
            if k == "1":
                c-=1
            else: c*=7
        if c == 489: print(prog)
