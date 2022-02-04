for t in range(10):
    dump_n = int(input())
    box_stack_lst = list(map(int, input().split()))
    for n in range(dump_n):
        # 현재 최대, 최저 높이 구하기
        max_stack = max(box_stack_lst)
        min_stack = min(box_stack_lst)

        # 최대에서 최저로 박스 1개 이동
        box_stack_lst[box_stack_lst.index(max_stack)] = max_stack - 1
        box_stack_lst[box_stack_lst.index(min_stack)] = min_stack + 1
    
    # 최종 높이 차이 출력
    print(f'#{t+1} {max(box_stack_lst) - min(box_stack_lst)}')
