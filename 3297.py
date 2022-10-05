x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
if max(abs(x1-x2), abs(y1-y2)) <= (r1+r2)/2: print("YES")
else: print("NO")