for t in range(10):
    N = int(input())
    building_lst = list(map(int, input().split()))
    view_count = 0
    # 양쪽 2칸 이내 최대 빌딩과의 높이 차이 더하기 (양쪽에 더 높은 빌딩 있으면 더하지 않음)
    for i in range(2, N-2):
        # 양 옆 빌딩 리스트
        side_buildings = building_lst[i-2:i+3]
        side_buildings.remove(building_lst[i])
        
        if building_lst[i] - max(side_buildings) > 0:
            view_count += building_lst[i] - max(side_buildings)
    
    print(f'#{t+1} {view_count}')
