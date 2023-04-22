Link : https://www.codechef.com/problems/BLACKJACK

Code :

for i in range(int(input())):
    x, y = map(int, input().split())
    z = x + y
    if z > 10:
        for i in range(1, 11):
            if (i + z) == 21:
                print(21 - z)
    else:
        print(-1)
