# 타겟에서 반대로 찾기
for t in range(10):
    N = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(input().split()))

    # 타겟 지점 x 좌표 찾기
    target_x = ladder[99].index('2')
    target_y = 99
    # 초기 움직임
    move = [0, -1]

    # 다 올라갈 때까지
    while target_y > 0:
        # 위로 올라가는 중일 때,
        if move[0] == 0:
            if target_x-1 >= 0 and ladder[target_y][target_x - 1] == '1':
                    move = [-1, 0]

            elif target_x+1 <= 99 and ladder[target_y][target_x + 1] == '1':
                    move = [1, 0]
        # 옆으로 움직이는 중일 때,    
        else:
            if ladder[target_y - 1][target_x] == '1':
                move = [0, -1]
        
        # 움직이기!
        target_x += move[0]
        target_y += move[1]

    print(f'#{N} {target_x}')