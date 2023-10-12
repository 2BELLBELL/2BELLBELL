from collections import deque
import copy
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
answer = []
wall_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([i, j])
        elif arr[i][j] == 1:
            wall_cnt += 1

for i in combinations(virus, M):
    q = deque(copy.deepcopy(i))
    visited = [[False] * N for _ in range(N)]
    for j in q:
        visited[j[0]][j[1]] = True
        j.append(0)

    while True:
        x, y, time = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] != 1:
                visited[nx][ny] = True
                q.append([nx, ny, time + 1])
        if not q:
            cnt = 0
            for i in range(N):
                cnt += visited[i].count(False)
            if cnt == wall_cnt:
                answer.append(time)
            break
if not answer:
    print(-1)
else:
    print(min(answer))