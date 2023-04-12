Link : https://www.codechef.com/problems/MAXTASTE

Code :

T = int(input())
for i in range(T):
    A, B, C, D = map(int, input().split())
    print(max((A + C), (A + D), (B + C), (B + D)))
