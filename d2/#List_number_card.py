T = int(input())
for t in range(T):
    N = int(input())
    num = input()
    max_count = 0
    for a in num:
        if num.count(a) > max_count:
            freq_num = a
            max_count = num.count(a)
        elif num.count(a) == max_count:
            if int(a) > int(freq_num):
                freq_num = a 
    print(f'#{t+1} {freq_num} {max_count}')
