import math

def factors(number):
    factsArray = []
    for i in range(1, int(math.sqrt(number)) + 1, 1):
        if number % i == 0:
            factsArray.append(i)
            factsArray.append(number // i)

    factsArray.sort()
    factsArray.pop()
    return factsArray

isPerfect = []

for i in range(2, 1001, 1):
    if sum(factors(i)) == i:
        isPerfect.append(i)

print('\n'.join(map(str, isPerfect)))
