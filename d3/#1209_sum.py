for t in range(10):
    N = int(input())
    array = []
    for i in range(100):
        array.append(list(map(int, input().split())))
    array_column = list(map(list,zip(*array)))

    max_sum = 0
    # 대각선 더하기
    diagnol1 = 0
    for n in range(100):
        diagnol1 += array[n][n]
    if diagnol1 > max_sum:
        max_sum = diagnol1
    
    # 역 대각선
    diagnol2 = 0
    for n in range(100):
        diagnol2 += array[n][99-n]
    if diagnol2 > max_sum:
        max_sum = diagnol1

    # 행
    for row in array:
        if sum(row) > max_sum:
            max_sum = sum(row)
    # 열
    for column in array_column:
        if sum(column) > max_sum:
            max_sum = sum(column)
    
    print(f'#{N} {max_sum}')