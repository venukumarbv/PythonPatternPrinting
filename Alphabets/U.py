'''
*       *
*       *
*       *
*       *
*       *
*       *
  * * *
'''
for row in range(7):
    for col in range(5):
        if row in range(6) and col in {0, 4}:
            print('*', end=' ')
        elif row == 6 and col in{1, 2, 3}:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
