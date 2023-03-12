Link : https://www.codechef.com/problems/CARTRIP

Code :

T = int(input())
for i in range(T):
    X = int(input())
    if X < 300:
        print(300*10)
    else:
        print(X*10)
