Link : https://www.codechef.com/problems/M1ENROL

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
    else:
        print(Y - X)
