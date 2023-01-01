Link : https://www.codechef.com/problems/TWODISH

Code :

T = int(input())
for i in range(T):
    dishes, fruits, vegetables, fishes = map(int, input().split())
    dishes_count = 0
    for i in range(dishes+1):
        if fruits != 0 and vegetables != 0:
            dishes_count += 1
            fruits -= 1
            vegetables -= 1
        if vegetables != 0 and fishes != 0:
            dishes_count += 1
            vegetables -= 1
            fishes -= 1

    if dishes_count >= dishes:
        print('YES')
    else:
        print("NO")
