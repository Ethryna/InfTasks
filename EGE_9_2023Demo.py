tabl = open('C:/Users/student/Documents/142Б/9.csv')
nums = []
ValL = []
numRep = 0
c = 0
RESLINES = 0
summ = 0
More = False
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
                if nums[i]==nums[j]:
                    if not c > 2:
                        c+=1
                        numRep = nums[i]
                    else:
                        More = True
                        break
                c = 0
        if More == False:
            ValL.append(nums)
        else: More = False
        for k in nums:
            if k != numRep:
                summ += int(k)
            if summ/4 <= 2*int(numRep):
                RESLINES += 1
        nums = []
        summ = 0
        numRep = 0
print(RESLINES)



