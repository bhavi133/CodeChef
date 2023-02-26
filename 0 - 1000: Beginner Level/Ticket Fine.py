Link : https://www.codechef.com/problems/TCKTFINE
  
Code :
  
T = int(input())
for i in range(T):
    X, P, Q = map(int, input().split())
    print(X*(P-Q))
