a = input()
b = a.replace('\\','\\\\').replace('\'','\\\'').replace('"','\\\"')
print(b)