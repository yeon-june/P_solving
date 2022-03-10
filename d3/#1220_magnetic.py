for t in range(1,11):
    N = int(input())
    array =[]
    for n in range(N):
        array.append(list(map(int, input().split())))
    # 열만 보기
    array_column = list(map(list,zip(*array)))
    cnt = 0
    # 교착상태 count (0빼고 12 베열찾기)
    for column in array_column:
        str_mags =''
        for num in column:
            # replace('0','') 도 가능, 0 제거
            if num != 0:
                str_mags += str(num)
        cnt += str_mags.count('12')
    print(f'#{t} {cnt}')
