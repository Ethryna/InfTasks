tabl = open('C:/Users/student/Documents/142Б/9.csv')
nums = []
numRep = 0
c = 0
r = 0
numsF = []
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
                if nums[i]==nums[j] and i != j and numRep == 0:
                    numRep = nums[i]
                    c = 1
                elif nums[i]==nums[j] and i != j and numRep != 0 and nums[i] != numRep:
                    c = 2
                    break
        if c == 1:
            for i in range(6):
                for j in range(6):
                    if nums[i]==nums[j] and i != j:
                        r += 1
            if r == 2:
                for k in nums:
                    if k != numRep:
                        summ+=int(k)
                if summ/4 <= 2*int(numRep):
                    RESLINES += 1
        nums = []
        numsF = []
        summ = 0
        numRep = 0
        c = 0
        r = 0

print(RESLINES)



