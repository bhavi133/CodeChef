Link : https://www.codechef.com/problems/PASSORFAIL

Code :

T = int(input())
for i in range(T):
    N, X, P = map(int, input().split())
    if (X * 3) - (N - X) >= P:
        print('PASS')
    else:
        print('FAIL')
