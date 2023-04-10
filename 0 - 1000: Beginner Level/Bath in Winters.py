Link : https://www.codechef.com/problems/BATH

Code :

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    print(X // (2 * Y))
