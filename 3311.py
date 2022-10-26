import sys
from collections import Counter
side_list = []
N, R = map(int,sys.stdin.readline().split())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
#(-R, R) 2차원 좌표에서 반지름 내부에 속하는 좌표를 배열에 append
for i in range(-R,R+1):
    for j in range(-R,R+1):
        side = ((i**2) +(j**2)) ** (1/2)
        if(side <= R):
            side_list.append((x+i,y+j))

# 좌표의 중복된 갯수 세기
counter = Counter(side_list)
# 사전순으로 앞서는 좌표 출력
print(counter.most_common()[0][0][0], end =' ')
print(counter.most_common()[0][0][1])

# #tmp=counter.most_common()
# tmp.sort(key=lambda x: (-x[1], x[0][0], x[0][1]))
# print(tmp[0][0][0], tmp[0][0][1], sep=' ')