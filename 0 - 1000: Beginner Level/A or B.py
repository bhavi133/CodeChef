Link : https://www.codechef.com/problems/AORB

Code :

T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    A = ((500-X*2)+(1000-(X+Y)*4))
    B = ((1000-Y*4)+(500-(X+Y)*2))
    print(max(A, B)) 
