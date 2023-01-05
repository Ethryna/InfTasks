with open('27_A.txt') as f:
    n=int(f.readline)
    s=[int(f.readline()) for i in range(n)] #?
    maximum,len_min=0,1000
    for i in range(n):
        summa=0
        for j in range(i+1,n):
            summa+=s[j]
            if summa%43==0:
                if summa>maximum or ((summa==maximum) and (j-i<len_min)):
                    maximum=summa
                    len_min=j-i
print(len_min)
