T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N <= M:
        short = A
        long = B
        sl = N
        ll = M
    else:
        short = B
        long = A
        sl = M 
        ll = N
    max_multi = 0
    for i in range(ll - sl +1):
        multi = 0
        for j in range(sl):
            multi += short[j]*long[i+j]
        if multi > max_multi:
            max_multi = multi
    print(f'#{t+1} {max_multi}')
