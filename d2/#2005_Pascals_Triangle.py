T = int(input())
# 테스트 케이스
for t in range(T):
    print(f'#{t+1}')
    N = int(input())
    # n번째 row 만들기
    for n in range(1, N+1):
        # base case (나중 join을 위해 str으로 저장)
        if n == 1:
            triangle = [['1']]
        # row 내부 생성
        else:
            # 공백 포함한 row 리스트 만들기 len(row) = 2n - 1
            new_row = [0 for j in range(2*n-1)]
            # row[m] 설정
            for m in range(2*n-1):
                # 양 옆은 1
                if m in [0, 2*n-2]:
                    new_row[m] = '1'
                # 홀수 인덱스 공백
                elif m % 2 == 1:
                    new_row[m] = ' '
                # 오른쪽, 왼쪽 위 (이전 row의 m-2, m 요소) 더하기
                else:
                    new_row[m] = str(int(triangle[n-2][m-2]) + int(triangle[n-2][m]))
            # 삼각형에 row 추가
            triangle.append(new_row)
    
    # 형식에 맞게 출력
    for j in range(N):
        print(''.join(triangle[j]))

