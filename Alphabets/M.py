'''
*       *
* *   * *
*   *   *
*       *
*       *
*       *
*       *
'''
for row in range(7):
    for col in range(5):
        if col in {0, 4}:
            print('*', end=' ')
        elif row == 1 and col in {1, 3}:
            print('*', end=' ')
        elif row == 2 and col == 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

        