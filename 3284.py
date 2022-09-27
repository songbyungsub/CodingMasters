from collections import deque
x=deque()
a=int(input())
x.append(0)
for i in range(1,a+1):
    b=input()
    if b=='U': x.append(i)
    elif b=='D': x.appendleft(i)
for i in range(a+1): print(x[i], end=" ")