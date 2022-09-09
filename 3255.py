import sys
size = list(map(int,sys.stdin.readline().split()))
M = []
N = []
for i in range(size[0]):
    M_2 = list(map(str,sys.stdin.readline().split()))
    M.append(M_2)
for i in range(size[0]):
    N_2 = list(map(str,sys.stdin.readline().split()))
    N.append(N_2)
c = M.copy()
for i in range(size[0]):
    for j in range(size[1]):
        if M[i][j] == N[i][j]:
            c[i][j] = M[i][j]
        if (ord(M[i][j]) + ord(N[i][j])) == ord('R') + ord('G'):
            c[i][j] = 'Y'
        if (ord(M[i][j]) + ord(N[i][j])) == ord('G') + ord('B'):
             c[i][j] = 'C'
        if (ord(M[i][j]) + ord(N[i][j])) == ord('B') + ord('R'):
            c[i][j] = 'M'
for i in range(size[0]):
    for j in range(size[1]):
        print(f'{c[i][j]}', end= ' ')
    print()