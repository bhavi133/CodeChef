Link : https://www.codechef.com/problems/EXPERT

Code :

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if ((Y / X) * 100) >= 50:
        print('YES')
    else:
        print('NO')
