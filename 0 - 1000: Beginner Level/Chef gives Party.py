Link : https://www.codechef.com/problems/PARTY2

Code :

T = int(input())
for i in range(T):
    N, X, K = map(int, input().split())
    if (N * X) <= K:
        print('YES')
    else:
        print('NO')
