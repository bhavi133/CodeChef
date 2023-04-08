Link : https://www.codechef.com/problems/TRUESCORE

Code :

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    if C >= A and D >= B:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
