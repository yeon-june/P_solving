'''
기본 아이디어
시작점과 도착점(start, end)이 있을 때, 
end에 속하지 않은 작업은 바로 작업 가능하므로, seq에 바로 추가
seq에 추가한 작업은 본인에게서 나가는 edge정보 삭제(idx를 받아서 start, end에서 해당 idx 지우기)
edge가 1개 남으면 (start, end 1개씩) edge순서대로 seq에 추가
마지막으로 처음부터 자신으로부터 뻗어나가는 edge가 없던 작업중 seq에 들어가지 않은 것이 있다면 추가(예외 처리)
'''

for t in range(10):
    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))

    start = []
    end = []
    for i in range(2*E):
        if i % 2:
            end.append(tmp[i])
        else:
            start.append(tmp[i])
    start1 = start[::]

    seq = []
    while len(start)>1:
        for i in range(1,V+1):
            if i not in seq:                # seq 에 없고
                if i not in end:            # 선행해야하는 작업이 없다면
                    seq.append(i)           # 추가하고
                    idxs = set()            # 추가한 작업으로부터 시작하는 edge 정보 지우기
                    try:
                        for j in range(E):
                            idxs.add(start.index(i,j))
                    except:
                        pass
                    idxs = list(idxs)
                    idxs.sort(reverse=True)
                    for idx in idxs:
                        del start[idx]
                        del end[idx]
            if len(start)==1:
                break

    seq.extend(start)
    seq.extend(end)
    # 뻗어나가는 edge가 없는 노드의 경우
    for star in set(range(1,V+1))-set(start1):
        # seq에 포함되지 않았다면 마지막에 추가
        if star not in seq:
            seq.append(star)

    print(f'#{t+1}',end=' ')
    print(*seq)


