'''
*       *
*       *
*       *
* * * * *
*       *
*       *
*       *
'''
for row in range(7):
    for col in range(5):
        if row != 3 and (col in {0, 4}):
            print('*', end=' ')
        elif row == 3:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()