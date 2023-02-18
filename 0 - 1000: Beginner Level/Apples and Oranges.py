Link : https://www.codechef.com/problems/APPLORNG

Code :

X = int(input())
A, B = map(int, input().split())
Y = A + B
if Y <= X:
    print('YES')
else:
    print('NO')
