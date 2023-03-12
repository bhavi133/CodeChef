Link : https://www.codechef.com/problems/TABLETS

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x * 3 <= y:
        print('YES')
    else:
        print('NO')
