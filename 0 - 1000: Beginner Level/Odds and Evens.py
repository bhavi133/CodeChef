Link : https://www.codechef.com/problems/ODDSEVENS

Code :

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if (X + Y) % 2 == 0:
        print('Bob')
    else:
        print('Alice')
