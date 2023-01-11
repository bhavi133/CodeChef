Link : https://www.codechef.com/problems/TALLER

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x > y:
        print('A')
    else:
        print('B')
