Link : https://www.codechef.com/problems/HIGHSCORE

Code :

T = int(input())
for i in range(T):
    N = int(input())
    Na, Nb, Nc, Nd = map(int, input().split())
    print(max(Na, Nb, Nc, Nd))
