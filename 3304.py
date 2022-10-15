str = input().strip()
a = int(input())
for _ in range(a):
    x, y, cur = input().split()
    cur = int(cur)
    str = str[0:cur] + str[cur:].replace(x, y, 1)
    print(str)