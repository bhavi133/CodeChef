Link : https://www.codechef.com/problems/MINHEIGHT

Code :

T = int(input())
for i in range(T):
    x, h = map(int, input().split())
    if x >= h:
        print('YES')
    else:
        print('NO')
