from random import randint
ans = randint(1,100)
isFound = False
guesses = 0

while not isFound:
    guess = int(input("Input a number between 1 and 100: "))
    guesses += 1
    if guess == ans:
        isFound = True
    elif guess > ans:
        print('too big')
    else:
        print('too small')

print(f'You got it! The number was {ans}')
print(f'It took you {guesses} guesses to get, the minimum number of guesses is 7 (using binary search).')
