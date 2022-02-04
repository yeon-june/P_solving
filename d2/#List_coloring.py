T = int(input())
for t in range(T):
    N = int(input())
    grid = [[0 for i in range(10)] for j in range(10)]

    for n in range(N):
        x1, y1, x2, y2, col = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2 +1):
                if grid[y][x] != col:
                    grid[y][x] += col
    purple = 0
    for row in grid:
        purple += row.count(3)
    
    print(f'#{t+1} {purple}')