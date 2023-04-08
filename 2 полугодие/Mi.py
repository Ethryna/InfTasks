a = input()
alf = ['м','и']
mat = [['***           ***','***    **    ***','***           ***','***           ***'],['***           ***','***     **   ***','***   **     ***','***           ***']]
l = []
for i in a:
    l.append(alf.index(i))
for k in range(4):
    print('')
    for j in l:
        print(mat[j][k], end='     ')
