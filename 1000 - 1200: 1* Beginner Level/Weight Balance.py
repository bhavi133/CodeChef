Link : https://www.codechef.com/problems/WEIGHTBL?tab=statement

Code :

T = int(input())
for i in range(T):
    w1, w2, x1, x2, m = map(int, input().split())
    z = w2 - w1
    if (z >= (m*x1)) and (z <= (m*x2)):
        print(1)
    else:
        print(0)
