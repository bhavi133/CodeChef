Link : https://www.codechef.com/problems/INVESTMENT

Code :

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if (Y * 2) <= X:
        print('YES')
    else:
        print('NO')
