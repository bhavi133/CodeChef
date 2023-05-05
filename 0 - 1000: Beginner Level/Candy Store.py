Link : https://www.codechef.com/problems/CANDYSTORE

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x >= y:
        print(y*1)
    else:
        print(x+(y-x)*2)
