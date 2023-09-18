def back(cost, num, x, y):
    global answer
    # 3개의 씨앗을 뿌렸으면 화단비용 체크
    if num == 3:
        answer = min(cost, answer)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            # 다른 꽃잎과 닿게 되는 경우는 패스
            flag = True
            for k, l in [[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]]:
                nx, ny = i + k, j + l
                if arr[nx][ny] == 999:
                    flag = False
            if not flag:
                continue
            # 꽃잎과 닿지 않는 구간인 경우 화단 비용을 더하고 씨앗의 위치를 999로 임시 지정
            cnt = arr[i][j] + arr[i - 1][j] + arr[i + 1][j] + arr[i][j - 1] + arr[i][j + 1]
            tmp_mid = arr[i][j]
            tmp_top = arr[i - 1][j]
            tmp_bot = arr[i + 1][j]
            tmp_left = arr[i][j - 1]
            tmp_right = arr[i][j + 1]
            arr[i][j] = arr[i - 1][j] = arr[i + 1][j] = arr[i][j - 1] = arr[i][j + 1] = 999
            back(cost + cnt, num + 1, i, j)
            arr[i][j] = tmp_mid
            arr[i - 1][j] = tmp_top
            arr[i + 1][j] = tmp_bot
            arr[i][j - 1] = tmp_left
            arr[i][j + 1] = tmp_right


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 최대 화단비용
answer = 3000000000
back(0, 0, 0, 0)
print(answer)