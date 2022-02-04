T = int(input())
for t in range(T):
    A, N = map(int, input().split())
    students = [i+1 for i in range(A)]
    assignment_lst = list(map(int, input().split()))
    # 전체 학생 리스트에서 제출 학생 지우기
    for student in assignment_lst:
        students.remove(student)
    print(f'#{t+1}', end = ' ')
    print(*students)