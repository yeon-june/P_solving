T = int(input())  # 테스트 케이스

GPA = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # GPA 저장
for t in range(T):
    N, K = map(int, input().split())
    scores = []
    total = []
    
    for n in range(N):
        scores.append(list(map(int,input().split())))                              # 학생마다 성적 리스트로 저장 
        final_s = 0.35 * scores[n][0] + 0.45 * scores[n][1] + 0.2 * scores[n][2]   # 최종 성적 계산
        total.append(final_s) # 최종 성적 리스트
    
    k_score = total[K-1]                                                           # K번째 학생 성적 저장   
    total.sort(reverse = True)                                                     # 학생 성적 정렬(내림차순)
    rank = total.index(k_score) + 1                                                # 학생 성적으로 석차 구하기

    gpa_idx = int((rank-1)//(N/10))                                                # 석차로 GPA index 구하기
    print(f'#{t+1} {GPA[gpa_idx]}')    
