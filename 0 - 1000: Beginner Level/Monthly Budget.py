Link : https://www.codechef.com/problems/BUDGET_

Code :

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    amount_spend = 30 * y
    if amount_spend <= x:
        print('YES')
    else:
        print("NO")
