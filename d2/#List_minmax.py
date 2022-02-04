T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    cur_max = lst[0]
    cur_min = lst[0]
    for n in range(N):
        if lst[n] > cur_max:
            cur_max = lst[n]
        if lst[n] < cur_min:
            cur_min = lst[n]
    
    print(f'#{t+1} {cur_max - cur_min}')