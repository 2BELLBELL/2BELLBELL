from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque([])

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    tmp_x, tmp_y = q.popleft()
    for i, j in [[-1, 0], [-1, -1], [-1, 1], [1, 1], [1, 0], [1, -1], [0, 1], [0, -1]]:
        nx, ny = tmp_x + i, tmp_y + j
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = arr[tmp_x][tmp_y] + 1
            q.append((nx, ny))

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, arr[i][j])
        
print(answer - 1)