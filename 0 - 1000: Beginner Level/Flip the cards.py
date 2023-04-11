Link : https://www.codechef.com/problems/FLIPCARDS

Code :

T = int(input())
for i in range(T):
    N, X = map(int, input().split())
    print(min(X, N-X))
