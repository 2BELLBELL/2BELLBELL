king, rock, N = input().split()
arr = [[0] * 8 for _ in range(8)]
word = 'ABCDEFGH'

# 킹과 돌의 위치 2차원 배열에 맞게 좌표로 변환
for i in king:
    if i in word:
        king_y = word.index(i)
    else:
        king_x = 8 - int(i)
for i in rock:
    if i in word:
        rock_y = word.index(i)
    else:
        rock_x = 8 - int(i)
# 킹과 돌 위치 넣기
arr[king_x][king_y] = 1
arr[rock_x][rock_y] = 2

for _ in range(int(N)):
    order = input()
    tmp_kx = king_x
    tmp_ky = king_y
    tmp_rx = rock_x
    tmp_ry = rock_y
    # 오른쪽이 벽이 아닌 경우
    if order == 'R' and 0 <= king_y + 1 < 8:
        # 돌이 없는 경우 바로 이동
        if arr[king_x][king_y + 1] == 0:
            king_y += 1
        # 돌이 있다면 돌도 벽을 넘는지 체크 후 이동
        else:
            if 0 <= king_y + 2 < 8:
                king_y += 1
                rock_y += 1
    # 왼쪽 이동
    elif order == 'L' and 0 <= king_y - 1 < 8:
        if arr[king_x][king_y - 1] == 0:
            king_y -= 1
        else:
            if 0 <= king_y - 2 < 8:
                king_y -= 1
                rock_y -= 1
    # 아래 이동
    elif order == 'B' and 0 <= king_x + 1 < 8:
        if arr[king_x + 1][king_y] == 0:
            king_x += 1
        else:
            if 0 <= king_x + 2 < 8:
                king_x += 1
                rock_x += 1
    # 위로 이동
    elif order == 'T' and 0 <= king_x - 1 < 8:
        if arr[king_x - 1][king_y] == 0:
            king_x -= 1
        else:
            if 0 <= king_x - 2 < 8:
                king_x -= 1
                rock_x -= 1
    # 오른쪽 위로 이동
    elif order == 'RT' and 0 <= king_x - 1 < 8 and 0 <= king_y + 1 < 8:
        if arr[king_x - 1][king_y + 1] == 0:
            king_x -= 1
            king_y += 1
        else:
            if 0 <= king_x - 2 < 8 and 0 <= king_y + 2 < 8:
                king_x -= 1
                king_y += 1
                rock_x -= 1
                rock_y += 1
    # 왼쪽 위로 이동
    elif order == 'LT' and 0 <= king_x - 1 < 8 and 0 <= king_y - 1 < 8:
        if arr[king_x - 1][king_y - 1] == 0:
            king_x -= 1
            king_y -= 1
        else:
            if 0 <= king_x - 2 < 8 and 0 <= king_y - 2 < 8:
                king_x -= 1
                king_y -= 1
                rock_x -= 1
                rock_y -= 1
    # 오른쪽 아래 이동
    elif order == 'RB' and 0 <= king_x + 1 < 8 and 0 <= king_y + 1 < 8:
        if arr[king_x + 1][king_y + 1] == 0:
            king_x += 1
            king_y += 1
        else:
            if 0 <= king_x + 2 < 8 and 0 <= king_y + 2 < 8:
                king_x += 1
                king_y += 1
                rock_x += 1
                rock_y += 1
    # 왼쪽 아래 이동
    elif order == 'LB' and 0 <= king_x + 1 < 8 and 0 <= king_y - 1 < 8:
        if arr[king_x + 1][king_y - 1] == 0:
            king_x += 1
            king_y -= 1
        else:
            if 0 <= king_x + 2 < 8 and 0 <= king_y - 2 < 8:
                king_x += 1
                king_y -= 1
                rock_x += 1
                rock_y -= 1

    arr[tmp_kx][tmp_ky], arr[tmp_rx][tmp_ry] = 0, 0
    arr[king_x][king_y] = 1
    arr[rock_x][rock_y] = 2


# 돌 좌표에서 출력용으로 재변환
king_last = ''
rock_last = ''
king_last += word[king_y]
king_last += str(8 - king_x)
rock_last += word[rock_y]
rock_last += str(8 - rock_x)
# 출력
print(king_last)
print(rock_last)