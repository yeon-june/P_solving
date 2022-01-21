N = int(input())
#출력에 사용할 result list
result = []

#1부터 N 까지 반복
for number in range(1,N+1):
    
    #int number을 str으로 변환
    str_number =str(number)

    #number에 3, 6, 9가 몇 번 나타나는지 count 할 변수
    count = 0
    
    #number의 길이만큼 반복
    for j in range(len(str_number)):
        #number 한 자리씩 확인하면서 3, 6, 9가 나올때마다 count + 1
        if int(str_number[j]) in [3, 6, 9]:
            count += 1
    
    # 3, 6, 9가 나오지 않는다면 숫자 출력
    if count == 0:
        result.append(str(number))
    
    # 3, 6, 9가 한번이라도 포함 돼 있다면 그 횟수만큼 '-' 출력
    else:
        result.append('-'*count)

#결과 print
print(' '.join(result))