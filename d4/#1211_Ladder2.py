def ladder_trace_back(ladder, start_idx, cur_min):
    target_x = start_idx
    target_y = 99
    # 초기 움직임
    move = [0, -1]
    cnt = 0
    # 다 올라갈 때까지
    while target_y > 0:
        # 앞선 최소보다 현재의 움직인 횟수가 커지면 break
        if cnt > cur_min:
            cnt = 100000
            break

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
        
        target_x += move[0]
        target_y += move[1]
        
        cnt +=1

    return [cnt, target_x]

for t in range(10):
    N = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(input().split()))
    
    min_dis = 100000000
    for i in range(100):
        if ladder[99][i] == '1':
            result = ladder_trace_back(ladder, i, min_dis)
            if min_dis > result[0]:
                min_dis = result[0]
                target_x = result[1]

    print(f'#{N} {target_x}')
