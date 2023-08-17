import sys

sys.setrecursionlimit(10 ** 5)


# 잠기지 않은 지역 개수 확인용
def dfs(x, y):
    visited[x][y] = False
    for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx = x + i
        ny = y + j
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == True:
            dfs(nx, ny)


N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_v = 0
for i in arr:
    if max_v < max(i):
        max_v = max(i)
max_cnt = 0
# 모두 잠기지 않을때부터 모두 잠기기 직전까지
for i in range(max_v):
    visited = [[True] * N for _ in range(N)]
    # i 이하의 지역은 잠긴다
    for j in range(N):
        for k in range(N):
            if arr[j][k] <= i:
                visited[j][k] = False

    cnt = 0
    for j in range(N):
        for k in range(N):
            if visited[j][k]:
                dfs(j, k)
                cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)