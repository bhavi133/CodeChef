Link : https://www.codechef.com/problems/SUMM

Code :

T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    if (a+b) == c:
        print('YES')
    else:
        print('NO')
