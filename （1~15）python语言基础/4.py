for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(5):
        if j < 5-i-1:
            print(' ',end = ' ')
        else:
            print('*',end = ' ')
    print()

for i in range(5):
    for _ in range(5 - i - 1):
        print(' ', end=' ')
    for _ in range(2 * i + 1):
        print('*', end=' ')
    print()
