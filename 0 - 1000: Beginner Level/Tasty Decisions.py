Link :

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    x = x * 2
    y = y * 5
    if x > y:
        print('Chocolate')
    elif x == y:
        print('Either')
    else:
        print('Candy')
