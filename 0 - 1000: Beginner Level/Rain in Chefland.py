Link : https://www.codechef.com/problems/RAINFALL1

Code :

T = int(input())
for i in range(T):
    x = int(input())
    if x < 3:
        print('LIGHT')
    elif x >= 3 and x < 7:
        print('MODERATE')
    elif x >= 7:
        print('HEAVY')
    else:
        pass
