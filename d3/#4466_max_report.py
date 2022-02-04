T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    total = 0
    for k in range(K):
        total += max(scores)
        scores.remove(max(scores))
    
    print(f'#{t} {total}')
