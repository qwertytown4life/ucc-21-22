def isLeap(x):
    if not x % 400:
        return True
    elif not x % 100:
        return False
    else: return not x % 4

year = 2021
cnt = 0
while cnt < 20:
    if isLeap(year):
        cnt += 1
        print(year)
    year += 1
