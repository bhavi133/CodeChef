Link : https://www.codechef.com/problems/LAZYCHF

Code :

for i in range(int(input())):
    x, y, z = map(int, input().split())
    print(min(x*y, x+z))
