Link : https://www.codechef.com/problems/BULLBEAR

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x < y:
        print('PROFIT')
    elif x == y:
        print('NEUTRAL')
    else:
        print('LOSS')
