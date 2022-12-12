tabl = open('C:/Users/student/Documents/142Б/9.csv')
nums = []
numRep = 0
r = 0
RESLINES = 0
summ = 0
EOF = False
while not EOF:
    s = tabl.readline()
    if not s:
        EOF = True
        break
    else:
        nums = (s[:len(s)-1].split(';'))
        for i in range(6):
            for j in range(6):
                for i in range(6):
                    if i!=j:
                        if nums[i]==nums[j]:
                            numRep = nums[i]
                            r+=1
            if r==2:
                for k in list(map(int,nums)):
                    if k!=int(numRep):
                        summ+=k
                if summ/4 <= 2*int(numRep):
                    RESLINES+=1
        nums = []
        summ = 0
        numRep = 0
        r = 0
        
print(RESLINES)
tabl.close()
