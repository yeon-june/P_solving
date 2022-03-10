T = int(input())
for t in range(T):
    recovery = list(input())
    N = len(recovery)
    bits = [0]*N
    for i in range(N):
        if recovery[i] == '1':
            first = i
            break
    
    change = 0
    for j in range(first, N):
        if bits[j] != recovery[j]:
            for k in range(j,N):
                bits[k] = recovery[j] 
            change += 1
        
        if bits == recovery:
            break

    print(f'#{t+1} {change}')