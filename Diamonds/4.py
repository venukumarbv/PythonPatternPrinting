'''
5
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1

'''
n = int(input())
# Upper half
for i in  range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(j+1,end=' ')
    print()

# Lower Half
for i in range(n-1):
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print(j+1,end=' ')
    print()