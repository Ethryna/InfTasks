print(min(list(n for n in range(100) if n*4+117 in [i for i in range(2,1000) if all(i%d!=0 for d in range(2,i-1))])))
