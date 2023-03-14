Link : https://www.codechef.com/problems/RACE400M

Code :

T = int(input())
for i in range(T):
    A, B, C = map(int, input().split())
    if 400 / A > 400 / B and 400 / A > 400 / C:
        print('ALICE')
    elif 400 / B > 400 / A and 400 / B > 400 / C:
        print('BOB')
    else:
        print('CHARLIE')
