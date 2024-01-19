import sys
input = sys.stdin.readline



def move_pin(x, y, n):
    global pin_num
    global move_num

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if n >= 0:
        if pin_num == 0 or pin_num > n:
            pin_num = n
            move_num = num - n

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 5 or ny >= 9:
                continue

            if map_input[nx][ny] == 'o':
                nnx = nx + dx[i]
                nny = ny + dy[i]

                if nnx < 0 or nny < 0 or nnx >= 5 or nny >= 9:
                    continue

                if map_input[nnx][nny] == '.':
                    map_input[x][y] = map_input[nx][ny] = '.'
                    map_input[nnx][nny] = 'o'

                    for k in range(5):
                        for j in range(9):
                            if map_input[k][j] == 'o':
                                move_pin(k, j, n - 1)

                    map_input[x][y] = map_input[nx][ny] = 'o'
                    map_input[nnx][nny] = '.'


T = int(input())
for _ in range(T):
    map_input = [list(input().strip()) for _ in range(5)]

    pin_num = move_num = 0
    count = 0
    for i in range(5):
        for k in range(9):
            if map_input[i][k] == 'o':
                count += 1
    num = count
    for i in range(5):
        for k in range(9):
            if map_input[i][k] == 'o':
                move_pin(i, k, count)

    try:
        input()
    except:
        pass
    print(pin_num, move_num)