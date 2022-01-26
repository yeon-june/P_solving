T = int(input())
# 테스트 케이스
for t in range(T):
    # N. M input
    N, M = map(int, input().split())
    # 파리 배치 array
    array = []
    # array 저장
    for n in range(N):
        array.append(list(map(int, input().split())))
    # 현재 최대
    cur_max = 0
    # (x,y)는 M*M의 첫번째 칸
    # x 범위 0 ~ N-M
    # y 범위 0 ~ N-M
    for x in range(N-M+1):
        for y in range(N-M+1):
            # 시작점 x, y 결정 후 fly_kill 초기화
            fly_kill = 0
            # 시작점에서 M*M 범위 내의 파리 수 더하기
            for m in range(y, M+y):
                for l in range(x, M+x):
                        fly_kill += array[m][l]
                
                # 현재의 최대보다 현재 파리 죽인 수가 클때, 최대 갱신
                if fly_kill > cur_max:
                    cur_max = fly_kill

    print(f'#{t+1} {cur_max}')


