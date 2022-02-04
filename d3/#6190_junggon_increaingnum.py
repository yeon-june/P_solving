def is_increasing(number):
    str_num = str(number)
    for i in range(len(str_num)-1):
        if str_num[i] > str_num[i+1]:
            return False
    return True
    
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    r = -1
    for i in range(N-1):
        for j in range(i+1, N):
            number = nums[i] * nums[j]
            if is_increasing(number):
                r = max(r,number)

    print(f'#{t} {r}')

