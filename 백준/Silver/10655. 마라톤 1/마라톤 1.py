import sys
input = sys.stdin.readline

N = int(input())
cp = [list(map(int, input().split())) for _ in range(N)]

# 전체 체크포인트의 합 구하기
cnt = 0
for i in range(1, N):
    cnt += abs(cp[i][0] - cp[i - 1][0]) + abs(cp[i][1] - cp[i - 1][1])

# 건너뛸 체크포인트
answer = cnt

for i in range(1, N - 1):
    # 빼야하는 경우의 수 1
    m1 = abs(cp[i][0] - cp[i - 1][0]) + abs(cp[i][1] - cp[i - 1][1])
    # 빼야하는 경우의 수 2
    m2 = abs(cp[i + 1][0] - cp[i][0]) + abs(cp[i + 1][1] - cp[i][1])
    # 더해야하는 경우의 수
    p = abs(cp[i + 1][0] - cp[i - 1][0]) + abs(cp[i + 1][1] - cp[i - 1][1])
    # 현재 체크포인트를 건너뛰는 거리
    dis = cnt - m1 - m2 + p

    if dis < answer:
        answer = dis
print(answer)