R = int(0)
N= int(0)
while not R>40:
    N = N+1
    N2S = str(bin(N))[2:]
    N2SO = N2S
    Sum = N2S.count('1')
    Rt=int(0)
    if Sum % 2 == 0:
        N2S = N2S+'0'
        RS = '10'+N2S[2:len(N2S)]
    if Sum % 2 == 1:
        N2S = N2S+'1'
        RS = '11'+N2S[2:len(N2S)]
    R = int(RS,2)
print(N)
