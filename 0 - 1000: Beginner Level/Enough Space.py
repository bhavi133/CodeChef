Link : https://www.codechef.com/problems/ENSPACE

Code :

T = int(input())
for i in range(T):
    n, x, y = map(int, input().split())
    x = x * 1
    y = y * 2
    if n >= (x + y):
        print('YES')
    else:
        print('NO')
