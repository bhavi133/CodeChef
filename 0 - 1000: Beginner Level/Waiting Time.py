Link : https://www.codechef.com/problems/WAITTIME

Code :

T = int(input())
for i in range(T):
    k, x = map(int, input().split())
    y = k * 7
    print(y - x)
