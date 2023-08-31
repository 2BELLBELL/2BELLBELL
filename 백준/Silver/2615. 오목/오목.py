def check(x, y, color):
    # 세로열 검사
    col = 0
    for i in range(1, 5):
        nx = x + i
        if nx < 19 and arr[nx][y] == color:
            col += 1
    up_down = True
    if col == 4:
        if x + 5 < 19 and arr[x + 5][y] == color:
            up_down = False
        if 0 <= x - 1 and arr[x - 1][y] == color:
            up_down = False
    if col == 4 and up_down:
        answer.extend([color, x, y])
        return
    # 가로열 검사
    row = 0
    for i in range(1, 5):
        ny = y + i
        if ny < 19 and arr[x][ny] == color:
            row += 1
    left_right = True
    if row == 4:
        if y + 5 < 19 and arr[x][y + 5] == color:
            left_right = False
        if 0 <= y - 1 and arr[x][y - 1] == color:
            left_right = False
    if row == 4 and left_right:
        answer.extend([color, x, y])
        return
    # 우 하 대각선 검사
    cross_down = 0
    for i in range(1, 5):
        nx, ny = x + i, y + i
        if nx < 19 and ny < 19 and arr[nx][ny] == color:
            cross_down += 1
    lu_rd = True
    if cross_down == 4:
        if x + 5 < 19 and y + 5 < 19 and arr[x + 5][y + 5] == color:
            lu_rd = False
        if 0 <= x - 1 and 0 <= y - 1 and arr[x - 1][y - 1] == color:
            lu_rd = False
    if cross_down == 4 and lu_rd:
        answer.extend([color, x, y])
        return
    # 우 상 대각선 검사
    cross_up = 0
    for i in range(1, 5):
        nx, ny = x - i, y + i
        if nx < 19 and ny < 19 and arr[nx][ny] == color:
            cross_up += 1
    ld_ru = True
    if cross_up == 4:
        if x - 5 < 19 and y + 5 < 19 and arr[x - 5][y + 5] == color:
            ld_ru = False
        if 19 > x + 1 and 0 <= y - 1 and arr[x + 1][y - 1] == color:
            ld_ru = False
    if cross_up == 4 and ld_ru:
        answer.extend([color, x, y])
        return

arr = [list(map(int, input().split())) for _ in range(19)]
answer = []

for i in range(19):
    for j in range(19):
        if arr[i][j]:
            check(i, j, arr[i][j])
            if answer:
                print(answer[0])
                print(answer[1] + 1, answer[2] + 1)
                exit()

print(0)