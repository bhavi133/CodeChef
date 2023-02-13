Link : https://www.codechef.com/problems/FAIRPASS

Code :

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    if K > N:
        print('YES')
    else:
        print('NO')
