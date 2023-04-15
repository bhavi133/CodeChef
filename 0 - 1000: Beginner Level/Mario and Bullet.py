Link : https://www.codechef.com/problems/BULLET

Code :

for i in range(int(input())):
    x, y, z = map(int, input().split())
    r = y // x
    if z - r < 0:
        print(0)
    else:
        print(z - r)
