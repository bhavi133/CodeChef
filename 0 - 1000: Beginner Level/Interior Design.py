Link : https://www.codechef.com/problems/INTRDSGN

Code :

T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    print(min((x1+y1), (x2+y2)))
