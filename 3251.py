import sys
import math
a = list(map(int,sys.stdin.readline().split()))
b = 0
for i in a:
    if i < 40:
        b = 1
c = sum(a) //5

if b != 1 and c >= 60:
    print("P")
else: print("F")
