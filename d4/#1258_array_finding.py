T = int(input())
for t in range(T):
    N = int(input())
    storage = []
    for n in range(N):
        storage.append(list(map(int, input().split())))

    # 사각형 시작점 찾기
    start_point = []        
    for x in range(N):
        for y in range(N):
            if x == 0 and y == 0 and storage[y][x] != 0:
                start_point.append([x,y])
            elif x == 0 and y != 0 and storage[y][x] != 0 and storage[y-1][x] == 0:
                start_point.append([x,y])
            elif y == 0 and x != 0 and storage[y][x] != 0 and storage[y][x-1] == 0:
                start_point.append([x,y])
            elif storage[y][x] != 0 and storage[y-1][x] == 0 and storage[y][x-1] == 0:
                start_point.append([x,y])
    
    # 사각형 찾기 [row, column, size] 저장
    squares = []
    for point in start_point:
        row = 1
        column = 1
        try:    
            for i in range(1,N):
                if storage[point[1]][point[0]+i] == 0:
                    break
                column += 1
        except:
            pass
        try:
            for j in range(1,N):
                if storage[point[1]+j][point[0]] == 0:
                    break
                row += 1
        except:
            pass
        size = row*column
        squares.append([row, column, size])
            
    # 2차 배열 sort, 2개 기준으로
    # 크기는 행과 열을 곱한 값으로, 크기가 작은 순서대로 출력한다.
    # 크기가 같을 경우 행이 작은 순으로 출력                 
    squares = sorted(squares, key = lambda x:(x[2], x[0]))

    print(f'#{t+1} {len(start_point)}', end = ' ')
    for r, c, s in squares:
        print(f'{r} {c}', end = ' ')
    print()

