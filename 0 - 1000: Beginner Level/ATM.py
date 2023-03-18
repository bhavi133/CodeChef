Link : https://www.codechef.com/problems/HS08TEST

Code :

x, y = map(float, input().split())
if (x + 0.50 <= y) and (x % 5 == 0):
    print("%.2f" %(y - x - 0.50))
else:
    print("%.2f" %(y))
