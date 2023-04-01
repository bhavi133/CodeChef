Link : https://www.codechef.com/problems/TODOLIST

Code :

for i in range(int(input())):
    x = int(input())
    l = list(map(int, input().split()))[:x]
    count = 0
    for i in l:
        if i >= 1000:
            count += 1
    print(count)
