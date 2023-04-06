Link : https://www.codechef.com/problems/MANGOES

Code :

T = int(input())
for i in range(T):
    X, Y, Z = map(int, input().split())
    print((Z-Y)//X)
