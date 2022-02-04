def count_palindrome(array):
    max_len = 0
    for row in array:
        for i in range(100):
            try:
                for N in range(100):    
                    word = row[i:i+N]
                    if word == word[::-1]:
                        if len(word) > max_len:
                            max_len = len(word)
            except:
                pass
        
    return max_len

for t in range(10):
    N = int(input())
    array = []
    for i in range(100):
        array.append(input())
    
    array_column = []
    for m in range(100):
        tmp =''
        for n in range(100):
            tmp+=array[n][m]
        array_column.append(tmp)
    
    print(f'#{N} {max(count_palindrome(array),count_palindrome(array_column))}')

