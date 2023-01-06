Link : https://www.codechef.com/problems/SNDMAX

Code :

n = int(input())
for i in range(n):
    l = list(map(int, input().strip().split()))[:n]
    print(sorted(l, reverse=True)[1])
