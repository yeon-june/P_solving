T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 중간 인덱스 mid (홀수로만 주어지니 경우 나눌필요 x)
    mid = N//2
    farm = [[] for n in range(N)]
    for m in range(N):
        for num in input():
            farm[m].append(int(num))

    # 전체 수 저장 변수
    crops = 0
    # 각 행마다 width
    width = 0
    # 중간까지 간격 늘리기, 다음 줄이기(마름모 만들기)
    for m in range(N):
        # 중간 이전에는 width 넓히기
        if m < mid:
            crops += sum(farm[m][mid-width:mid+width+1])
            width += 1
        
        # 중간 이후에는 width 좁히기
        else:
            crops += sum(farm[m][mid-width:mid+width+1])
            width -= 1
    
    print(f'#{t} {crops}')


    
