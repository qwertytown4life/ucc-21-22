from random import randint
l = sorted([randint(1,1000) for i in range(100)])
print(l)
print((l[49] + l[50]) // 2)
