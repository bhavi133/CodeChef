Link : https://www.codechef.com/problems/WINNERR

Code :

T = int(input())
for i in range(T):
    Pa, Pb, Qa, Qb = map(int, input().split())
    X = max(Pa, Pb)
    Y = max(Qa, Qb)
    if X < Y:
        print('P')
    elif X == Y:
        print('TIE')
    else:
        print('Q')
