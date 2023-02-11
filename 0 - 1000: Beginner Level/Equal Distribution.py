Link : https://www.codechef.com/problems/EQUALDIST

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x == y:
        print('YES')
    elif (x + y) % 2 == 0:
        print('YES')
    else:
        print('NO')
