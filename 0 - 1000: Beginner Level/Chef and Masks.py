Link : https://www.codechef.com/problems/CMASKS

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if (x*100) < (y*10):
        print('Disposable')
    else:
        print('Cloth')
