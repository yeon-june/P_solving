T = int(input())
for t in range(T):
    N = int(input())
    num_lst = list(range(1,N+1))
    zigzag_num = 0
    for i in range(N):
        if i % 2:
            zigzag_num -= num_lst[i]
        else:
            zigzag_num += num_lst[i]
    
    print(f'#{t+1} {zigzag_num}')
