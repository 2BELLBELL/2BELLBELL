import sys
input = sys.stdin.readline

# 로봇 청소기 작동
def clean(x, y, z):
    move = [[x, y, z]]
    arr[x][y] = 2
    cnt = 1
    while True:
        # 현재 좌표 / 방향을 변수로 선언
        tmp_x, tmp_y, tmp_z = move.pop()
        # 현재 방향의 반시계부터 네 방향 탐색
        for i in range(4):
            nx = tmp_x + news[(tmp_z + 3) % 4][0]
            ny = tmp_y + news[(tmp_z + 3) % 4][1]
            # 청소 안된곳을 찾았으면 청소/카운트 증가/해당 좌표 추가 후 중지
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                cnt += 1
                move.append([nx, ny, (tmp_z + 3) % 4])
                break
            else:
                tmp_z = (tmp_z + 3) % 4
        # 현재 좌표의 네 방향이 모두 청소되어 있으면
        if not move:
            nx = tmp_x + news[(tmp_z + 2) % 4][0]
            ny = tmp_y + news[(tmp_z + 2) % 4][1]
            # 현재 방향의 뒤쪽이 청소한곳이면 방향 유지한채로 뒤로 이동
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 2:
                move.append([nx, ny, tmp_z])
            # 뒤가 벽이라면 종료
            else:
                break

    return cnt

N, M = map(int, input().split())
robot_x, robot_y, robot_d = map(int, input().split())
news = [[-1, 0], [0, 1], [1, 0], [0, -1]]
arr = [list(map(int, input().split())) for _ in range(N)]
print(clean(robot_x, robot_y, robot_d))