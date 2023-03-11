#сортировка пузырьком

L = [2,23,90,0,24,4,723,456,24,347,7,34,2]
done = False
flag = False
while done == False:
    c=0
    for i in range(len(L)-1):
        a = L[i]
        b = L[i+1]
        if a>b:
            L[i+1]=a
            L[i]=b
            c+=1
        if ((i == (len(L)-2)) and c==0):
            print(L)
            done = True
