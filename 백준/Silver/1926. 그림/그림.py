import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    global total
    total += 1
    arr[x][y] = 0

    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx = x+i
        ny = y+j
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
            dfs(nx, ny)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
max_v = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            total = 0
            dfs(i, j)
            cnt += 1
            if total > max_v:
                max_v = total

print(cnt)
print(max_v)