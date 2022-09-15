k = int(input())
N=0
if k % 2== 1:
    N = k+1
else: N = k+2

a = N//2

if a % 2== 0:
    N +=2
else: N = N
print(N)

