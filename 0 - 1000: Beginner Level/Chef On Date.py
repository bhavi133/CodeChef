Link : https://www.codechef.com/problems/CHEFONDATE

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x >= y:
        print('YES')
    else:
        print('NO')
