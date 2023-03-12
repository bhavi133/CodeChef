Link : https://www.codechef.com/problems/SIXFRIENDS

Code :

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    print(min((X*3), (Y*2)))
