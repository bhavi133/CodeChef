Link : https://www.codechef.com/problems/FOOTCUP

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x >= 1 and y >= 1 and x == y:
        print('YES')
    else:
        print('NO')
