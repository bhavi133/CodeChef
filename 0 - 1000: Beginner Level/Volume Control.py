Link : https://www.codechef.com/problems/VOLCONTROL

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    print(max(x, y)-min(x, y))
