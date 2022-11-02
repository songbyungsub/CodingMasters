import sys

lst = list(map(int, sys.stdin.readline().strip()))
check = "NO"
if lst[0]+lst[1] == lst[2]+lst[3]:
    check = "YES"
elif lst[0]+lst[2] == lst[1]+lst[3]:
    check = "YES"
elif lst[0]+lst[3] == lst[1]+lst[2]:
    check = "YES"
print(check)