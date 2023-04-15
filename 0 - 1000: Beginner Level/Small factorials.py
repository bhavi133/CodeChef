Link : https://www.codechef.com/problems/FCTRL2

Code :

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

T = int(input())
for i in range(T):
    N = int(input())
    print(fact(N))
