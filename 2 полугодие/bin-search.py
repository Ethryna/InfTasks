L = [x for x in range(1000000,0,-1)]
leng = len(L)
mid = leng//2
start = 0
end = leng
M = 0
work = True
while work == True:
    mid = start+(end-start)//2
    print(start, mid, end)
    if end-mid>1:
        if L[mid]>L[mid+1]:
            start = mid
            if L[mid+1]!=M: M = L[mid+1]
            else:
                print(M)
                work = False
        else:
            end = mid
            if L[mid]!=M: M = L[mid]
            else:
                print(M)
                work = False
    else:
        if mid>end:
            start = mid
            if L[end]!=M: M = L[end]
            else:
                print(M)
                work = False
        else:
            end = mid
            if L[mid]!=M: M = L[mid]
            else:
                print(M)
                work = False
            
