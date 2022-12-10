gl = {'A','O'}
sogl = {'C','D','F'}
sflag = False
c=0
k=0
with open('24.txt') as f:
    s=f.readline()
    for i in range(len(s)):
        if (s[i]in sogl)==True:
            if sflag == False:
                sflag = True
            elif sflag == True:
                if c>k:
                    k = c
                c = 0
        elif (s[i]in gl)==True:
            if sflag == True:
                c+=1
                sflag = False
            elif sflag == False:
                if c>k:
                    k = c
                c = 0
print(k)
