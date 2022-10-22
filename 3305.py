a = int(input())
aw = [[1]]
for i in range(1, a):
    flag = [[0 for _ in range(i+1)] for _ in range(i+1)]
    for x in range(i):
        for y in range(i):
            flag[x][y] += aw[x][y]
            flag[x+1][y] += aw[x][y]
            flag[x][y+1] += aw[x][y]
    aw.clear()
    aw = flag
    
for i in range(len(aw)):
    for j in range(len(aw)-i):
        print(aw[i][j], end=" ")
    print()