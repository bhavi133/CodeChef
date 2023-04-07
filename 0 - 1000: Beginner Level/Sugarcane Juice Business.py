Link : https://www.codechef.com/problems/SUGARCANE

Code :

for i in range(T):
    X = int(input())
    Y = 50 * X
    A = Y * 0.2
    B = Y * 0.2
    C = Y * 0.3
    print(int(Y - (A + B + C)))
