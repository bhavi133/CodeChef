Link : https://www.codechef.com/problems/POLTHIEF

Code :

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if X >= Y:
        print(X - Y)
    else:
        print(Y - X)
