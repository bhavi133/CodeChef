Link : https://www.codechef.com/problems/POPULATION

Code :

T = int(input())
for i in range(T):
    X, Y, Z = map(int, input().split())
    print(X-Y+Z)
