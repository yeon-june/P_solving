def change_cal(money):
    change = []
    for m in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        change.append(money//m)
        money = money % m
    
    return change

T = int(input())
for t in range(T):
    money = int(input())
    print(f'#{t+1}')
    print(*change_cal(money))
