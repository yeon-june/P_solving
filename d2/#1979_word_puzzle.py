T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    # 행 저장
    puzzle_row = []
    for n in range(N):
        puzzle_row.append(list(map(int, input().split())))
    # 열 저장
    puzzle_column = list(map(list,zip(*puzzle_row)))

    


    # 들어갈 수 있는 곳 count
    cnt = 0
    for i in range(N):
        # 1을 만나면 row_count +1 0 만나면 reset/ 3연속을 찾기위해
        if sum(puzzle_row[i]) >= K:
            row_cnt = 0
            for j in range(N):
                if puzzle_row[i][j] == 1:
                    row_cnt +=1
                else:
                    if row_cnt == K:
                        cnt +=1
                    row_cnt = 0
            if row_cnt == K:
                cnt += 1
        if sum(puzzle_column[i]) >= K:
            column_cnt = 0
            for j in range(N):
                if puzzle_column[i][j] == 1:
                    column_cnt +=1
                else:
                    if column_cnt == K:
                        cnt +=1
                    column_cnt = 0
            if column_cnt == K:
                cnt += 1               

    
    print(f'#{t+1} {cnt}')
