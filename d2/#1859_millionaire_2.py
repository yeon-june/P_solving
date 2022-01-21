T = int(input())

for t in range(T):
    N= int(input())
    price = list(map(int,input().split()))
    cur_max = max(price)
    profit = 0
    for i in range(N-1):
        if price[i] == cur_max:
            cur_max = max(price[i+1:])
        else:
            profit += cur_max - price[i]
    
    print(f'#{t+1} {profit}')