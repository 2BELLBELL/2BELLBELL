from collections import deque

M, N, H = map(int, input().split())
# 3차원 배열로 입력 받기
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
que = deque()
flag = True
# 3차원 배열을 순회하며 익어있는 토마토를 q에 삽입하기
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                que.append([h, i, j])
            if arr[h][i][j] == 0:
                flag = False
# 이미 전부 익어있으면 0 출력
if flag:
    print(0)
    exit()
else:
    # bfs 실행
    while que:
        tmp_z, tmp_x, tmp_y = que.popleft()
        # 해당 층의 델타 탐색 후 익을 수 있는 위치면 익히기
        for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = i + tmp_x
            ny = j + tmp_y
            if 0 <= nx < N and 0 <= ny < M and arr[tmp_z][nx][ny] == 0:
                arr[tmp_z][nx][ny] = arr[tmp_z][tmp_x][tmp_y] + 1
                que.append([tmp_z, nx, ny])
        # 위 아래층도 익을 수 있으면 익히기
        for i in [-1, 1]:
            nz = i + tmp_z
            if 0 <= nz < H and arr[nz][tmp_x][tmp_y] == 0:
                arr[nz][tmp_x][tmp_y] = arr[tmp_z][tmp_x][tmp_y] + 1
                que.append([nz, tmp_x, tmp_y])
    
    # 아직 안 익은게 있으면 -1 출력
    day = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    print(-1)
                    exit()
                elif arr[h][i][j] > day:
                    day = arr[h][i][j]
    # 다 익었으면 며칠 걸렸는지 출력
    print(day-1)