Link : https://www.codechef.com/problems/TESTAVG

Code :

T = int(input())
for i in range(T):
    X, Y, Z = map(int, input().split())
    if ((X + Y) // 2) < 35 or ((Y + Z) // 2) < 35 or ((X + Z) // 2) < 35:
        print('FAIL')
    else:
        print('PASS')
