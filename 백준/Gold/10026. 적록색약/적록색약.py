import sys
sys.setrecursionlimit(10**9)
# 적록색약이 아닌 경우
def dfs_rgb(x, y):
    color = arr[x][y]
    if color in ['R', 'G']:
        arr[x][y] = 1
    else:
        arr[x][y] = 0

    for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        nx = i+x
        ny = j+y
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == color:
            dfs_rgb(nx, ny)

# 적록색약인 경우
def dfs_rg_b(x, y):
    color = arr[x][y]
    arr[x][y] = 3

    for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        nx = i+x
        ny = j+y
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == color:
            dfs_rg_b(nx, ny)

N = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt1 = 0

# 적록색약이 아닌 사람이 봤을때
for i in range(N):
    for j in range(N):
        if arr[i][j] in ['R', 'G', 'B']:
            dfs_rgb(i, j)
            cnt1 += 1
print(cnt1, end=' ')

# 적록색약인 사람이 봤을때
cnt2 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] in [1, 0]:
            dfs_rg_b(i, j)
            cnt2 += 1

print(cnt2)