def f(x1,x2,start,end):
    count=0
    ls=[]
    for k in range(x1,x2):
        for i in range(2**k):
            b=bin(i)[2:]
            b=(k-len(b)-1)*'0' +b
            res=start
            for y in range(len(b)):
                if b[y] =='0': 
                    res+=1
                elif b[y] =='1':
                    res=res*2
                if res>35:break
                if res==17:break
                if res==16 and y<len(b)-1 and b[y+1]=='0':break
            if res==end:
                if not ls.count(b)>0:
                    ls.append(b)
                    count+=1
                    print(k, b, res, count)
    return count
count1=count2=0

start=2
end=10
count1=f(3,10,start,end)

start=10
end=35
count2=f(10,18,start,end)
print(count1*count2*2)
