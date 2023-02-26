Link : https://www.codechef.com/problems/AIRHOCKEY
  
Code :
  
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    print(7-max(x, y))
