Link : https://www.codechef.com/problems/AUCTION

Code :

T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    if a > b and a > c:
        print('Alice')
    elif b > c and b > a:
        print('Bob')
    else:
        print('Charlie')
