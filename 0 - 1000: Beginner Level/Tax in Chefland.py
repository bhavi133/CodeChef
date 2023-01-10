Link : https://www.codechef.com/problems/TAXES

Code :

T = int(input())
for i in range(T):
    x = int(input())
    if x > 100:
        print(x - 10)
    else:
        print(x)
