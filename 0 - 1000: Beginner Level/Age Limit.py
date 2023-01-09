Link : https://www.codechef.com/problems/AGELIMIT

Code :

T = int(input())
for i in range(T):
    lower_limit, upper_limit, age = map(int, input().split(' '))
    if age >= lower_limit and age < upper_limit:
        print('YES')
    else:
        print('NO')
