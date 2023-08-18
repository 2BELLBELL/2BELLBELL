N, M = map(int, input().split())

# 2차원 배열로 받아준다
arr = [list(map(int, list(input()))) for _ in range(N)]

# 현재 좌표부터 bfs 시작
que = [0, 0]
# 이동 횟수는 음수로 계산
arr[0][0] = -1
while que:
    # 큐에서 좌표를 pop 한다
    tmp_x = que.pop(0)
    tmp_y = que.pop(0)
    # 상하좌우 델타탐색
    for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx = i+tmp_x
        ny = j+tmp_y
        # 벽을 넘었는지 체크
        if 0 <= nx < N and 0 <= ny < M:
            # 이동 가능한 경우 해당 위치를 음수 이동 횟수로 갱신하고 큐에 좌표 삽입
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[tmp_x][tmp_y] -1
                que.append(nx)
                que.append(ny)

# N과 M을 인덱스로 활용하기 위해 -1씩 해주고
# 양수로 전환하기 위해 -1을 곱하여 출력
print(arr[N-1][M-1]*-1)