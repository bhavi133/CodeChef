Link : https://www.codechef.com/problems/MISSP

Code :

T = int(input())
for i in range(T):
    n = int(input())
    arr = []
    for i in range(0, n):
        element = int(input())
        arr.append(element)
    for i in arr:
        if arr.count(i) % 2 != 0:
            print(i)
            break
