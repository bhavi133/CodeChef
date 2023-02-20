Link : https://www.codechef.com/problems/COMPLEXITY

Code :

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    if A > B:
        print('YES')
    else:
        print('NO')
