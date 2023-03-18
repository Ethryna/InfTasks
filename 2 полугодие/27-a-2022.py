with open('27_B.txt') as f:
    nums = list(map(int,f.readlines()))
    s = 0
    smax = 0
    l = 0
    for i in nums:
        if i%43==0:
            s+=i
            l+=1
            if s>smax:
                smax = s
                lmax = l
        else:
            s = 0
            l = 0
print(lmax)
