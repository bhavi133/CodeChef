Link : https://www.codechef.com/problems/AIRLINE

Code : 

T = int(input())
for i in range(T):
    a, b, c, d, e = map(int, input().split())
    if (a + c <= d) and (b <= e):
        print('YES')
    elif (a + b <= d) and (c <= e):
        print('YES')
    elif (b + c <= d) and (a <= e):
        print('YES')
    else:
        print('NO')
