#2007. 패턴 마디의 길이

T= int(input())
for t in range(T):

    period_str = input()
            
    #문자열 시작 문자
    first_chr = period_str[0]
    #시작문자와 같은 문자의 인덱스를 저장할 리스트
    same_chr_idx = []

    #같은 문자 인덱스 모두 찾기 
    #str.find(문자, 시작 인덱스) -> 시작점으로부터 최초로같은 인덱스 하나만 나옴
    for i in range(1,len(period_str)):
            same_chr_idx.append(period_str.find(first_chr, i))
    #set으로 중복 제거
    idx_set = set(same_chr_idx)

    #세트에 있는 인덱스를 기준으로 반복점 찾기
    for number in idx_set:
        if period_str[:number] == period_str[number:2*number] and period_str[2*number:3*number] == period_str[number:2*number]:
            period = number
            break
    #결과 출력
    print(f'#{t+1} {period}')


