Link : https://www.codechef.com/problems/ELECTIONS?tab=statement

Code :

T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    if a > 50:
        print('A')
    elif b > 50:
        print('B')
    elif c > 50:
        print('C')
    else:
        print('NOTA')
