from collections import deque

def bfs():
    q = deque()
    q.append(start)
    visited = [[False] * N for _ in range(N)]
    size = 2
    exp = 2
    answer = 0
    while q:
        x, y, time = q.popleft()
        if arr[x][y] < size and arr[x][y] != 0:
            while q:
                xx, yy, timetime = q.popleft()
                if timetime == time and arr[xx][yy] != 0 and arr[xx][yy] < size:
                    if xx < x:
                        x, y = xx, yy
                    elif xx == x and yy < y:
                        y = yy
            arr[x][y] = 0
            exp -= 1
            answer += time
            time = 0
            visited = [[False] * N for _ in range(N)]
            if exp == 0:
                size += 1
                exp = size

        for i, j in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] <= size:
                visited[nx][ny] = True
                q.append((nx, ny, time + 1))

    return answer


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 아기상어의 시작 위치 탐색
for i in range(N):
    flag = True
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            start = (i, j, 0)
            flag = False
            break
    if not flag:
        break

print(bfs())