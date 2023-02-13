Link : https://www.codechef.com/problems/MAXDIFFMIN

Code :

T = int(input())
for i in range(T):
    A, B, C = map(int, input().split())
    print(max(A, B, C) - min(A, B, C))
