def serv_possible(customer, M, K):
    # 첫손님 기준 가능, 불가능
    if customer[0] < M:
        return 'Impossible'
    
    bbang = 0
    for sec in range(customer[-1]+1):
        # M초 마다 붕어빵 만들기
        if sec != 0 and sec % M == 0:
            bbang += K
        # 손님에게 붕어빵 팔기
        for cus in customer:
            if sec == cus:
                bbang -= 1
                # 팔 붕어빵이 없으면 불가능
                if bbang < 0:
                    return 'Impossible'
    # 기본값 가능
    return 'Possible'



T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    # 오는 순서대로 정렬
    customer.sort()

    print(f'#{t} {serv_possible(customer, M, K)}')
