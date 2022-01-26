'''
[key idea]
N*N의 기본 행렬이 존재하고, 시계방향으로 움직이는 movement를 정의하고 움직일때마다 각 칸에 숫자 저장
'''

T = int(input())
#테스트 케이스 마다
for t in range(T):
    print(f'#{t+1}')
    N = int(input())
    P = N
    # 기본 행렬 생성
    array = [[1 for j in range(N)] for i in range(N)]
    '''
    예시  N = 2
    array = [[1, 1]
             [1, 1]]
    '''
    # 시작 숫자
    num = 1
    # 시작 좌표 x,y
    x = -1
    y = 0
    # movement와 이동 길이를 위한 edge(turn) 정보 변수
    turn = 0
    # 이동길이가 0 이상일때,
    while N > 0:
        # edge별 x,y movement
        if turn % 4 == 1:
            x_move = 0
            y_move = 1
        elif turn % 4 == 2:
            x_move = -1
            y_move = 0
        elif turn % 4 == 3:
            x_move = 0
            y_move = -1
        else:
            x_move = 1
            y_move = 0                

        # edge의 이동길이만큼 이동 및 숫자 저장
        for i in range(N):
            x += x_move
            y += y_move
            array[y][x] = num
            num += 1 
        # edge를 다 지나면 turn + 1
        turn += 1

        # 2번 turn하면 이동 길이 - 1
        if turn % 2 :
            N -= 1
    # 결과 프린트
    for k in range(P):
        for p in range(P):
            print(array[k][p], end = ' ')
        print()