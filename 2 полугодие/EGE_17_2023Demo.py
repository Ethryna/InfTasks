with open('17.txt') as f:
   nums=[int(x) for x in f]
   maxi=[]
   s=[]
   
   for i in range(0,len(nums)):
      if nums[i]%10==3:
         maxi.append(nums[i])
   maximum=0
  
   for i in range(len(nums)-1):
      if ((abs(nums[i])%10==3) and (abs(nums[i+1])%10!=3)) or ((abs(nums[i])%10!=3) and (abs(nums[i+1])%10==3)):
         if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
               s.append(nums[i]+nums[i+1])
               if nums[i]**2+nums[i+1]**2>maximum:
                  maximum=nums[i]**2+nums[i+1]**2
   print(len(s), maximum)

   
   
   
   
   
#OR
   
with open('17.txt') as f:
a = [int(x) for x in f]

b = list(reversed(sorted(a)))
for i in b:
    if abs(i)%10==3:
        KV = i**2
        break

c=0
sKV = 0

for i in range(len(a)-1):
    if (((abs(a[i])%10==3 and abs(a[i+1])%10!=3) or (abs(a[i])%10!=3 and abs(a[i+1])%10==3)) and (a[i]**2+a[i+1]**2>=KV)):
        c+=1
        if (a[i]**2+a[i+1]**2)>sKV:
            sKV = a[i]**2+a[i+1]**2

print(c, sKV)
