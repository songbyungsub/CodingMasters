a = int(input())
b = a
cnt = 0

while b > 10:
    if b % 10 == 3 or b % 10 == 6 or b % 10 == 9:
        cnt += 1
    if b // 10 == 3 or b // 10 == 6 or b // 10 == 9:
        cnt += 1
    b = b // 10
    if b < 10: break

if cnt:
    print('clap' * cnt)
elif a == 3 or a == 6 or a ==9:
    print('clap')
else : print(a)