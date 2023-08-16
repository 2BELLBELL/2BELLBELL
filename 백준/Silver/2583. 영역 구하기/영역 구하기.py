import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

# 모눈종이 채우기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            arr[i][j] = 1

# 상하좌우 체크하며 1로 채우기
def dfs(x, y):
    arr[x][y] = 1
    for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx = i+x
        ny = j+y
        if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
            global size
            size += 1
            dfs(nx, ny)

# 채운 횟수와 넓이
cnt = 0
size_lst = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            size = 1
            dfs(i, j)
            size_lst.append(size)
            cnt += 1

print(cnt)
print(*sorted(size_lst))