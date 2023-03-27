Link : https://www.codechef.com/problems/PROINC

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    k = x - y
    l = x * 10 // 100
    print((x+l)-(k))
