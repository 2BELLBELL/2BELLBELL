from collections import deque

def bfs(x, y, crashed):
    # 벽을 부쉈는지 안부쉈는지 3차원 배열로 확인
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    q = deque([x, y, crashed])
    visited[x][y][crashed] = 1
    while q:
        tmp_x = q.popleft()
        tmp_y = q.popleft()
        tmp_crashed = q.popleft()
        # 도착지에 도착했다면
        if tmp_x == N - 1 and tmp_y == M - 1:
            return visited[tmp_x][tmp_y][tmp_crashed]
        for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx = tmp_x + i
            ny = tmp_y + j
            # 맵을 안넘었고, 안가본 통로가 있다면
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny][tmp_crashed] == 0:
                q.append(nx)
                q.append(ny)
                q.append(tmp_crashed)
                visited[nx][ny][tmp_crashed] = visited[tmp_x][tmp_y][tmp_crashed] + 1
            # 맵을 안넘었고, 벽이 있고, 벽을 이전에 안부쉈다면
            elif 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and tmp_crashed == 0:
                q.append(nx)
                q.append(ny)
                q.append(1)
                visited[nx][ny][1] = visited[tmp_x][tmp_y][0] + 1

    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(bfs(0, 0, 0))