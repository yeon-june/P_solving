# 테스트 횟수 받기
T = int(input())
for t in range(T):
    # 출력 형식 맞추기
    print(f'#{t+1}')

    # N*N 행렬의 N 값 받기
    N = int(input())

    # input값을 row 단위로 정리
    row_list = []

    for n in range(N):
        row_list.append(list(input().split()))
    # row_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 90도 돌리기 시작: 모든 행렬은 row 단위로 정리
    # rowN, row N-1, ... 순서로 세로로 출력 -> [row[n][1], row[n-1][1]...] 형식으로 묶을 예정
    new_row_list90 = []
    for j in range(N):
        # 각 row를 저장할 내부 리스트 추가
        new_row_list90.append([])
        # N번째~ row의 j번째 요소를 한 리스트로 묶기 아래 예시! 
        for i in range(N-1,-1,-1):
            new_row_list90[j].append(row_list[i][j])
    # new_row_list1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # 90도를 90도 돌리기
    new_row_list180 = []
    for j in range(N):
        new_row_list180.append([])
        for i in range(N-1,-1,-1):
            new_row_list180[j].append(new_row_list90[i][j])


    # 180도를 90도 돌리기
    new_row_list270 = []
    for j in range(N):
        new_row_list270.append([])
        for i in range(N-1,-1,-1):
            new_row_list270[j].append(new_row_list180[i][j])

    # 형식에 맞게 출력, 각 리스트 안의 n번째 리스트가 각 회전 경우마다의 n번째줄 
    for row in range(N):
        print(f'{"".join(new_row_list90[row])} {"".join(new_row_list180[row])} {"".join(new_row_list270[row])}')