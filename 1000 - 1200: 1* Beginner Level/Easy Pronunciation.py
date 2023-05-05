Link : https://www.codechef.com/problems/EZSPEAK

Code :

T = int(input())
vowel = 'aeiou'
for _ in range(T):
    n = int(input())
    word = input()
    count = 0
    arr = []
    if n < 4:
        print("YES")
    else:
        for i in word:
            if i in vowel:
                arr.append(count)
                count = 0
            else:
                count+=1
        arr.append(count)
        if max(arr)>3:
            print("NO")
        else:
            print("YES")
