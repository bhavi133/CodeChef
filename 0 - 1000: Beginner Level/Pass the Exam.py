Link : https://www.codechef.com/problems/PASSTHEEXAM

Code :

T = int(input())
for i in range(T):
    x, y, z = map(int, input().split())
    if (x >= 10) and (y >= 10) and (z >= 10) and (x + y + z >= 100):
        print("PASS")
    else:
        print("FAIL")
