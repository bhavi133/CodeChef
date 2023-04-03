Link : https://www.codechef.com/problems/ACTEMP

Code :

T = int(input())
for i in range(T):
    A, B, C = map(int, input().split())
    if B >= A and B >= C:
        print('Yes')
    else:
        print('No')
