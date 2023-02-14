Link : https://www.codechef.com/problems/READPAGES

Code :

T = int(input())
for i in range(T):
    N, X, Y = map(int, input().split())
    if N <= (X*Y):
        print('YES')
    else:
        print('NO')
