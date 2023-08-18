T = int(input())

for tc in range(1, T + 1):
    l = int(input())
    x, y = map(int, input().split())
    x2, y2 = map(int, input().split())
    # l x l 의 배열 생성
    arr = [[0] * l for _ in range(l)]
    que = [x, y]
    # bfs 진행
    while que:
        tmp_x = que.pop(0)
        tmp_y = que.pop(0)
        # 목적지를 찾았다면 최소 이동 횟수 출력
        if tmp_x == x2 and tmp_y == y2:
            print(arr[tmp_x][tmp_y])
            break
        # 나이트의 이동 8방향 처리 
        for i, j in [[-2, -1], [-2, 1], [-1, -2], [-1, 2],
                     [1, -2], [1, 2], [2, -1], [2, 1]]:
            nx = i + tmp_x
            ny = j + tmp_y
            # 벽을 안넘고 안가본 곳인 경우
            if 0 <= nx < l and 0 <= ny < l and arr[nx][ny] == 0:
                # 현재까지 이동 횟수 체크
                arr[nx][ny] = arr[tmp_x][tmp_y] + 1
                # 현재 좌표 큐에 삽입하기
                que.append(nx)
                que.append(ny)