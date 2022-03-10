# 전체 탐색
def change_count(flag, M, w, b, r):
    change = 0
    for i in range(w):
        change += M - flag[i].count('W')
    for j in range(w, w+b):
        change += M - flag[j].count('B')
    for k in range(w+b,w+b+r):
        change += M - flag[k].count('R')
    return change




T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    flag = []
    for n in range(N):
        flag.append(input())

    min_change = 20000
    # 가능한 (w,b,r) 을 2중 for 문으로 구성
    for w in range(1, N - 2 +1):
        for b in range(1, N - w):
            r = N - w - b
            if change_count(flag, M, w, b, r) < min_change:
                min_change = change_count(flag, M, w, b, r)
                
    
    print(f'#{t+1} {min_change}')
            
