import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y):
    global wolf, sheep
    visited[x][y] = True
    if farm[x][y] == 'v':
        wolf += 1
    elif farm[x][y] == 'o':
        sheep += 1
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        if farm[nx][ny] == '#' or visited[nx][ny]:
            continue
        dfs(nx, ny)


R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
totalwolf, totalsheep = 0, 0
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(R):
    for j in range(C):
        if farm[i][j] == "#" or visited[i][j]:
            continue
        wolf, sheep = 0, 0
        dfs(i, j)
        if wolf >= sheep:
            totalwolf += wolf
        else:
            totalsheep += sheep

print(totalsheep, totalwolf)