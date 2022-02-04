# test case
T = int(input())
for t in range(T):
    result = 1
    # input 받기 (row 저장)
    sdoku_row =[]
    for n in range(9):
        sdoku_row.append(list(map(int, input().split())))
    # column 저장
    sdoku_column = list(map(list, zip(*sdoku_row)))
    
    # square 저장
    sdoku_new_row = [[],[],[],
                    [],[],[],
                    [],[],[]]
    for n in range(9):
        for m in range(3):
            sdoku_new_row[n].append(list(sdoku_row[n][3*m:3*m+3]))


    first = [sdoku_new_row[0],sdoku_new_row[1],sdoku_new_row[2]]
    second = [sdoku_new_row[3],sdoku_new_row[4],sdoku_new_row[5]]
    third = [sdoku_new_row[6],sdoku_new_row[7],sdoku_new_row[8]]

    first_squares = list(map(list,zip(*first)))
    second_squares =  list(map(list, zip(*second)))
    third_squares = list(map(list, zip(*third)))
    for i in range(3):
        first_squares[i] = (first_squares[i][0]+first_squares[i][1] +first_squares[i][2])
        second_squares[i] = (second_squares[i][0]+second_squares[i][1] +second_squares[i][2])
        third_squares[i] = (third_squares[i][0]+third_squares[i][1] +third_squares[i][2])
    
    # 가로/ 세로/ square 검정
    for k in range(1,10):
        for a in sdoku_row:
            if a.count(k) != 1:
                result = 0
                break
        if result == 0:
            break
        for b in sdoku_column:
            if b.count(k) != 1:
                result = 0
                break
        if result == 0:
            break        
        
        for j in range(3):
            if first_squares[j].count(k) != 1:
                result = 0
                break
            if second_squares[j].count(k) != 1:
                result = 0
                break
            if third_squares[j].count(k) != 1:
                result = 0
                break

    print(f'#{t+1} {result}')
