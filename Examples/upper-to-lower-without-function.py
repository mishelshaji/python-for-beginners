s = 'Hello World'
res = ''
for c in s:
    if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        res = res + c
    else:
        k = ord(c)
        l = k + 32
        res = res + chr(l)

print(res)
