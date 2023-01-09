Link : https://www.codechef.com/problems/DETSCORE

Code :

T = int(input())
for i in range(T):
    x, n = map(int, input().split())
    if x % 10 == 0:
        y = x // 10
        print(y*n)
    else:
        pass
