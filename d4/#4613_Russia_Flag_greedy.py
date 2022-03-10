# greedy
def from_front(flag, N, M):
    change = 0
    change += M - flag[0].count('W')
    change += M - flag[N-1].count('R')
    flag[0] = 'W'*M
    flag[N-1] = 'R'*M
    org_flag_sec = flag[N-2]

    for i in range(1,N-1):
        if flag[i-1][0] == 'W':
            if flag[i].count('W')>= flag[i].count('B'):
                letter = 'W'
                change += M - flag[i].count('W')
            else:
                letter = 'B'
                change += M - flag[i].count('B')
            flag[i] = letter*M

        elif flag[i-1][0] == 'B':
            if flag[i].count('B')>= flag[i].count('R'):
                letter = 'B'
                change += M - flag[i].count('B')
            else:
                letter = 'R'
                change += M - flag[i].count('R')
            flag[i] = letter*M
        
        else:
            letter = 'R'
            change += M - flag[i].count('R')
            flag[i] = letter*M
        flag=flag[::]

    cnt = 0
    for row in flag:
        if row[0] == 'B':
            cnt += 1
    if cnt == 0:
        change += M - org_flag_sec.count('B') - (M - org_flag_sec.count('W'))

    return change


def from_back(flag, N, M):
    change = 0
    change += M - flag[0].count('W')
    change += M - flag[N-1].count('R')
    org_flag_sec = flag[1]
    flag[0] = 'W'*M
    flag[N-1] = 'R'*M

    for i in range(N-2,0,-1):
        if flag[i+1][0] == 'R':
            if flag[i].count('R')>= flag[i].count('B'):
                letter = 'R'
                change += M - flag[i].count('R')
            else:
                letter = 'B'
                change += M - flag[i].count('B')
            flag[i] = letter*M
            flag=flag[::]

        elif flag[i+1][0] == 'B':
            if flag[i].count('B')>= flag[i].count('W'):
                letter = 'B'
                change += M - flag[i].count('B')
            else:
                letter = 'W'
                change += M - flag[i].count('W')
            flag[i] = letter*M
            flag=flag[::]
        else:
            letter = 'W'
            change += M - flag[i].count('W')
            flag[i] = letter*M
            flag=flag[::]

    cnt = 0
    for row in flag:
        if row[0] == 'B':
            cnt += 1
    if cnt == 0:
        change += M - org_flag_sec.count('B') - (M - org_flag_sec.count('R'))

    return change

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    flag = []
    for n in range(N):
        flag.append(input())
    flag1 = flag[::]
    print(f'#{t+1} {min(from_front(flag, N, M),from_back(flag1, N, M))}')


            
