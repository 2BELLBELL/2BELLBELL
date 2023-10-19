'''
거리를 기준으로 이분 탐색
'''

d, n, m = map(int, input().split())
stone = [0, d]
cha = []
for _ in range(n):
    stone.append(int(input()))
stone.sort()

start = 0
end = d

while start <= end:
    # 돌섬 사이의 최소거리
    mid = (start + end) // 2
    # 돌섬의 인덱스
    idx = 1
    # 없애야하는 돌섬의 개수
    cnt = 0

    while n + 2 > idx:
        # 점프해야하는 거리
        jump = stone[idx] - stone[idx - 1]
        # 돌섬 사이의 최소거리보다 작다면 없애야 하는 작은 섬
        if jump < mid:
            while jump < mid:
                cnt += 1
                idx += 1
                if idx == n + 2:
                    break
                jump += stone[idx] - stone[idx - 1]
        # 돌섬 사이의 최소거리보다 같거나 크다면 다음 섬으로 이동
        idx += 1


    if cnt <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)