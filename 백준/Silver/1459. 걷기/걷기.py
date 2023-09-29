x, y, w, s = map(int, input().split())
answer = 0
# 한 블록씩 이동 하는게 더 빠른 경우
if w < s:
    # 대각선에 있는 블록을 한 블록씩 가는게 더 빠른 경우
    if 2 * w < s:
        answer += (x + y) * w
    # 대각선에 있는 블록은 가로질러서 가는게 더 빠른 경우
    elif 2 * w >= s:
        # 좌표가 하나라도 0에 맞물릴때까지 대각선 이동
        if x <= y:
            answer += (x * s)
            y -= x
            x = 0
        else:
            answer += (y * s)
            x -= y
            y = 0
        # 이후 남은 좌표 직선 이동
        answer += (x + y) * w
# 대각선 이동이 더 빠른 경우
elif w >= s:
    if not (x + y) % 2:
        answer += max(x, y) * s
    else:
        answer += max(x, y) * s + w - s

print(answer)