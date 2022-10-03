for w in range(1,3):
	Wt = w-1
	for x in range(1,3):
		Xt = x-1
		for y in range(1,3):
			Yt = y-1
			for z in range(1,3):
				Zt = z-1
				F = ((not(y<=x)) or (z<=w) or (not(z)))
				if F == False:
				    print (f'Функция {F}, wxyz {Wt}{Xt}{Yt}{Zt}')
