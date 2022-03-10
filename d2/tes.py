def solution(new_id):
    valid_id = []
    valid = ['-', '_', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # 애초에 빈문자
    if not new_id:
        return 'aaa'
    
    # 4단계-1 마침표가 처음
    s_idx = 0
    if new_id[0] == '.':
        if set(new_id) == {'.'}:
            return 'aaa'
        
        while 1:
            if new_id[s_idx] != '.':
                break
            else:
                s_idx += 1
    
    for i in range(s_idx, len(new_id)):            
        # 1단계 대문자 -> 소문자
        # 2단계 사용가능한 문자 외 문자 제거
        if new_id[i].isalpha():
            valid_id.append(new_id[i].lower())
        elif new_id[i] in valid:
            valid_id.append(new_id[i])
            
        # 3단계 마침표 2번 이상, 마침표 1개로 치환
        if new_id[i-1] == '.' and new_id[i] == '.':
            valid_id.pop()
    
    # 6단계, 15자 이상 문자 지우기
    if len(valid_id) > 15:
        valid_id = valid_id[:15]
          
    # 4단계-2 마침표가 끝이면 제거
    if valid_id[-1] == '.':
        if set(valid_id) == {'.'}:
            return 'aaa'
        
        while valid_id:
            if valid_id[-1] != '.':
                break
            else:
                valid_id.pop()
    # 5단계 빈문자열 -> 'a'
    if not valid_id:
        valid_id.append('a')
        
    # 7단계 2자 이하, new_id 마지막 문자 3될때까지 반복
    if len(valid_id) < 3:
        while len(valid_id) < 3:
            valid_id.append(valid_id[-1])
            
    answer = ''.join(valid_id)
    return answer

print(solution('.1.'))



def solution(new_id):
    valid = ['-', '_', '.']
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for char in new_id:
        if char in valid or char.isdigit() or char.isalpha():
            answer += char
    # 3
    while '..' in answer:
        answer.replace('..', '.')
    
    #4 
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    #5
    if not answer:
        answer += 'a'
    
    #6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    
    #7
    while len(answer) < 3:
        answer += answer[-1]
    return answer