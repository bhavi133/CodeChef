Link : https://www.codechef.com/problems/PRIZEPOOL

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    l = ((10*x) + (90*y))
    print(l)
