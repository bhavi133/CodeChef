Link : https://www.codechef.com/problems/FINE

Code :

T = int(input())
for i in range(T):
    X = int(input())
    if X <= 70:
        print(0)
    elif X > 70 and X <= 100:
        print(500)
    else:
        print(2000)
