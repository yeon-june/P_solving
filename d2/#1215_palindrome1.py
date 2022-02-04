def count_palindrome(N, array):
    cnt = 0
    for row in array:
        for i in range(len(row)-N+1):
            word = ''.join(row[i:i+N])
            if word == word[::-1]:
                cnt += 1
    
    return cnt



for t in range(1,11):
    N = int(input())
    array = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        s = input()
        for j in range(8):
            array[i].append(s[j])
    
    array_column = list(map(list,zip(*array)))

    print(f'#{t} {count_palindrome(N,array)+count_palindrome(N,array_column)}')
