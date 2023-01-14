Link : https://www.codechef.com/problems/MY1STCONTEST

Code :

n, a, b = map(int, input().split())
l = []
x = n - a
y = x - b
l.append(x)
l.append(y)
for i in l:
    print(i, end=" ")
