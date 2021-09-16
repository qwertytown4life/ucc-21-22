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

def factors(number):
    factsArray = []
    for i in range(1, int(math.sqrt(number)) + 1, 1):
        if number % i == 0:
            factsArray.append(i)
            factsArray.append(number // i)

    factsArray.sort()
    factsArray.pop()
    return factsArray

N = int(input())
if isPrime(N):
    print(f"{N} is prime!")
else:
    print(' '.join(map(str, factors(N))))
