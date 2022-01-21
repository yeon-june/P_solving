T = int(input())

for t in range(T):
    N= int(input())
    price = list(map(int, input().split()))
    
    #알고 미래의 날이 1일 이하, profit = 0
    if len(price) <2:
        profit = 0
    else:
        #총 구매 금액, 기간 중 최대 가격, 구매 횟수 초기 값 설정
        buy = 0
        count = 0
        profit = 0
        cur_max = max(price)
        for i in range(len(price)-1):
            # 오늘 가격이 내일 가격보다 작다면 구매 금액에 오늘의 금액을 더하고, 구매 횟수를 더한 후 최대 값 갱신
            if price[i] <= price[i+1]:
                buy += price[i]
                count += 1
            else:
                if price[i] == max(price):
                    profit += price[i] * count - buy
                    count =0
                    buy =0
                    cur_max = max(price[i+1:])

         
        
        profit += cur_max* count - buy
        
        print(f'#{t+1} {profit}')