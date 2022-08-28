a = int(input())
b=a
print(f'{b} ', end ='')
while(a > 1):
    if a % 2 ==0:
        a = a//2
    else:
        a = 3* a + 1
    print(f'{a} ',end='')