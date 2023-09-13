import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global flag
    visieted[x][y] = True
    q = deque([(x, y)])
    stack = [[x, y]]
    stack_sum = arr[x][y]
    while q:
        tmp_x, tmp_y = q.popleft()
        for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = tmp_x + i, tmp_y + j
            if 0 <= nx < N and 0 <= ny < N and \
                    visieted[nx][ny] == False and \
                    L <= abs(arr[nx][ny] - arr[tmp_x][tmp_y]) <= R:
                q.append((nx, ny))
                stack.append([nx, ny])
                stack_sum += arr[nx][ny]
                visieted[nx][ny] = True
                flag = False

    for i, j in stack:
        arr[i][j] = stack_sum // len(stack)

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    visieted = [[False] * N for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            if not visieted[i][j]:
                bfs(i, j)

    if flag:
        print(cnt)
        break

    cnt += 1