Link : https://www.codechef.com/problems/AMR15A

Code :

x = int(input())
l = list(map(int, input().split()))[:x]
even_count = 0
odd_count = 0
for i in l:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print('READY FOR BATTLE')
else:
    print('NOT READY')   
