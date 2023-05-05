Link : https://www.codechef.com/problems/SCALENE

Code :

T = int(input())
for i in range(T):
    side1, side2, side3 = map(int, input().split(' '))
    if side1 != side2 and side2 != side3 and side3 != side1:
        print('YES')
    else:
        print('NO')
