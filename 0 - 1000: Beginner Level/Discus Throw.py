Link : https://www.codechef.com/problems/DISCUS

Code :

T = int(input())
for i in range(T):
    X, Y, Z = map(int, input().split())
    print(max(X, Y, Z))
