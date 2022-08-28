a = input()
flag = 0
for i in a:
    if i == '.':
        flag = 1
    elif i == ':':
        flag = 2
if flag == 1:
    print('IPv4')
elif flag ==2:
    print('IPv6')