def back(pick, num):
    global answer
    # 10개를 전부 찍었다면
    if num == 10:
        cnt = 0
        for i in range(10):
            if arr[i] == int(pick[i]):
                cnt += 1
        if cnt >= 5:
            answer += 1
        return

    # 찍기 시작
    for j in range(1, 6):
        if len(pick) >= 2 and pick[-1] == pick[-2] == str(j):
            continue
        back(pick + str(j), num + 1)

arr = list(map(int, input().split()))
answer = 0
back('', 0)
print(answer)