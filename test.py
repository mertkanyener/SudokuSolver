import copy

l1 = [1,2,3]
l2 = copy.copy(l1)

l2 = [1,2]
print(l1)


def sth(a):
    a = 3
    return True

print(sth(4))
