from collections import deque

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    arr[x][y] = False
    while q:
        tmp_x, tmp_y = q.popleft()
        for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = i + tmp_x, j + tmp_y
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]:
                arr[nx][ny] = False
                q.append((nx, ny))
                cnt += 1

N, M, K = map(int, input().split())
arr = [[False] * M for _ in range(N)]
answer = 0
for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = True

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            cnt = 1
            bfs(i, j)
            answer = max(answer, cnt)

print(answer)