T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    min_sum = 10000000
    max_sum = 0    
    for n in range(N-M+1):
        sub_tot = 0
        for m in range(M):
            sub_tot += lst[n+m]
        
        if sub_tot < min_sum:
            min_sum = sub_tot
        if sub_tot > max_sum:
            max_sum = sub_tot
    
    print(f'#{t+1} {max_sum - min_sum}')


