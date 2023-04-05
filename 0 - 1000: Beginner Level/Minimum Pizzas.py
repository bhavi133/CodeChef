Link : https://www.codechef.com/problems/MINPIZZA

Code :

import math

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    print(math.ceil((X * Y) / 4))
