def serv_possible(customer, M, K):
    if customer[0] < M:
        return 'Impossible'
    
    bbang = 0
    for sec in range(customer[-1]+1):
        if sec != 0 and sec % M == 0:
            bbang += K
        for cus in customer:
            if sec == cus:
                bbang -= 1
                if bbang < 0:
                    return 'Impossible'
    return 'Possible'



T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()

    print(f'#{t} {serv_possible(customer, M, K)}')
