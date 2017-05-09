sth = "000100208"
res = []
for i in sth:
    if i == '0':
        res.append(set(range(1, 10)))
    else:
        res.append(set(range(int(i), int(i) + 1)))

print(res)