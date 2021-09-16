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
N = int(input())
if N == 1:
    print("1 is not perfect.")
elif sum(factors(N)) == N:
    print(f"{N} is perfect!")
else:
    print(f"{N} is not perfect.")
