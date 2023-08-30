board = [[0] * 6 for _ in range(6)]
word = 'ABCDEF'
y, x = input()
x = 6 - int(x)
y = word.index(y)
first_x, first_y = x, y
start = [[x, y]]
board[x][y] = 1
answer = 'Valid'
for _ in range(35):
    y, x = input()
    x = 6 - int(x)
    y = word.index(y)

    # 이전 좌표의 8방향 탐색 경로에 있는지 체크
    flag = False
    before_x, before_y = start.pop()
    for i, j in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, -1], [-2, 1]]:
        nx, ny = before_x + i, before_y + j
        if 0 <= nx < 6 and 0 <= ny < 6 and nx == x and ny == y:
            flag = True
    if not flag:
        answer = 'Invalid'

    start.append([x, y])
    if board[x][y] == 0:
        board[x][y] = board[before_x][before_y] + 1
    else:
        answer = 'Invalid'

# 시작 좌표와 끝 좌표가 8방향 경로에 있는지 체크
flag = False
for i, j in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, -1], [-2, 1]]:
    nx, ny = first_x + i, first_y + j
    if 0 <= nx < 6 and 0 <= ny < 6 and nx == x and ny == y:
        flag = True
if not flag:
    answer = 'Invalid'

print(answer)