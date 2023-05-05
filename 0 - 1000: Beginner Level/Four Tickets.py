Link : https://www.codechef.com/problems/FOURTICKETS

Code :

T = int(input())
for i in range(T):
    X = int(input())
    if X * 4 <= 1000:
        print('YES')
    else:
        print('NO')
