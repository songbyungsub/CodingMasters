# 1=가위 2=바위 3=보
import sys
n = int(input())
score_1 =0
score_2 =0
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    if a[0] == 1:
        if a[1] == 2:
            score_2 +=1
        elif a[1] == 3:
            score_1 +=1
    elif a[0] == 2:
        if a[1] == 1:
            score_1 +=1
        elif a[1] == 3:
            score_2 +=1
    elif a[0] == 3:
        if a[1] == 1:
            score_2 +=1
        elif a[1] == 2:
            score_1 +=1
print(f'{score_1} {score_2}')