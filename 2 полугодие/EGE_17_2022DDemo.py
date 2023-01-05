with open('17.txt') as f:
    numbers=[int(x) for x in f]
    l = []
    s=[]
    
    for k in numbers:
      if k%3==0: 
        l.append(k)
    m = max(l)
    
    for i in range(1,len(numbers)):
        if numbers[i]%3==0 or numbers[i-1]%3==0:
            if numbers[i]+numbers[i-1]<=m: 
              s.append(numbers[i]+numbers[i-1])
print(len(s), max(s))
