a = int(input())
lst = list(map(int,input().split()))
c = sum(lst) % a
mean = sum(lst) // a

check = 0
for i in range(a):
    check += abs(mean-lst[i])
print((check-c) // 2 + c)