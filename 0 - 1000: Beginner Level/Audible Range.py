Link : https://www.codechef.com/problems/AUDIBLE

Code :

T = int(input())
for i in range(T):
    x = int(input())
    if x >= 67 and x <= 45000:
        print('YES')
    else:
        print('NO')
