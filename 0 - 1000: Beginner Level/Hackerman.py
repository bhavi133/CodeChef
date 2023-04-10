Link : https://www.codechef.com/problems/PRIMEDICE

Code :

def is_prime(n):
    if n == 1:
        return 1
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
            
def func():
    if is_prime(x+y):
        return 'Alice'
    else:
        return 'Bob'

for i in range(int(input())):
    x, y = map(int, input().split())
    print(func())
