Link : https://www.codechef.com/problems/CRICMATCH

Code :

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    if N > ((M * 6) * 6):
        print('NO')
    else:
        print('YES')
