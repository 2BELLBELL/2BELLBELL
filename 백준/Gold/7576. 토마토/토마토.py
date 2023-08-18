from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
que = deque()
flag = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append(i)
            que.append(j)
        if arr[i][j] == 0:
            flag = False

if flag:
    print(0)
    exit()
else:
    while que:
        tmp_x = que.popleft()
        tmp_y = que.popleft()
        for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = i + tmp_x
            ny = j + tmp_y
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = arr[tmp_x][tmp_y] + 1
                que.append(nx)
                que.append(ny)

    day = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                print(-1)
                exit()
            elif arr[i][j] > day:
                day = arr[i][j]

    print(day-1)
