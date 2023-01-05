with open('24.txt') as f:
    s=f.readline()
    count,maximum=1,0
    for i in range(1,len(s)):
        if s[i]==s[i-1]=='P':
            count=1
        else:
            count+=1
            maximum=max(maximum,count)
print(maximum)
