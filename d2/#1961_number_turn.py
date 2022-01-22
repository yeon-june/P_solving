N = int(input())

row_list = []

for n in range(N):
    row_list.append(list(map(int, input().split())))
# row_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_row_list90 = []
for j in range(N):
    new_row_list90.append([])
    for i in range(N-1,-1,-1):
        new_row_list90[j].append(row_list[i][j])
# new_row_list1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

new_row_list180 = []
for j in range(N):
    new_row_list180.append([])
    for i in range(N-1,-1,-1):
        new_row_list180[j].append(new_row_list90[i][j])

new_row_list270 = []
for j in range(N):
    new_row_list270.append([])
    for i in range(N-1,-1,-1):
        new_row_list270[j].append(new_row_list180[i][j])


for row in range(N):
    print(f'{"".join(map(str,new_row_list90[row]))} {"".join(map(str,new_row_list180[row]))} {"".join(map(str,new_row_list270[row]))}')