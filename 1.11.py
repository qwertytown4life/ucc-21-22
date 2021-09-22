for i in range(1, 13, 1):
    for j in range(1, 13, 1):
        res = str(i * j)
        spaces = 3 - len(res)
        print(spaces * ' ' + res, end=' ')
    print()
    
