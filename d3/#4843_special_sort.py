T = int(input())
for t in range(T):
    N = int(input())
    num_lst = list(map(int, input().split()))
    num_lst.sort()
    special_sort = []
    while len(special_sort)<10:
        # 오름차순 정렬된 리스트의 맨 뒤, 맨 앞을 리스트에 저장하고 지우기
        special_sort.append(num_lst.pop())
        special_sort.append(num_lst.pop(0))
    
    print(f'#{t+1}', end = ' ')
    print(*special_sort)
