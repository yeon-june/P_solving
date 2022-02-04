T = int(input())
for t in range(1, T+1):
    N = int(input())
    mid = N//2
    farm = [[] for n in range(N)]
    for m in range(N):
        for num in input():
            farm[m].append(int(num))

    crops = 0
    width = 0
    # 중간까지 간격 늘리기, 다음 줄이기(마름모 만들기)
    for m in range(N):
        if m < mid:
            crops += sum(farm[m][mid-width:mid+width+1])
            width += 1
        
        else:
            crops += sum(farm[m][mid-width:mid+width+1])
            width -= 1
    
    print(f'#{t} {crops}')


    
