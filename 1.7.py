import math
def isPrime(n):
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

x = 2
cnt = 0

while cnt < 100:
    if isPrime(x):
        print(x)
        cnt += 1
    x += 1
