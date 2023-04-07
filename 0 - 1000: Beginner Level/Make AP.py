Link : https://www.codechef.com/problems/MAKEAP

Code :

T = int(input())
for i in range(T):
    A, C = map(int, input().split())
    if (A + C) % 2 == 0:
        print((A + C) // 2)
    else:
        print(-1)
