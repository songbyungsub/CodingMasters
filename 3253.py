import sys
import math
a = list(map(int,sys.stdin.readline().split()))
m = max(a)
a.remove(m)
print(a[0] * a[1] //2)