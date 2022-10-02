str = input().strip()
result = list()
for i in range(len(str)):
    for j in range(i+1, len(str)+1):
        if len(str) % (j-i) == 0:
            tmp = str[i:j]
            if str == tmp * (len(str) // (j-i)):
                result.append(tmp)
result.sort()
print(result[0])