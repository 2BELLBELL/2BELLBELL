import sys
input = sys.stdin.readline

'''
DP문제 *어려움

1. 각각의 체크포인트 사이의 거리 생성
2. K개를 건너뛴다면 갈 수 있는 최소거리 갱신 
'''

N, K = map(int, input().split())
cp = [list(map(int, input().split())) for _ in range(N)]

# 각 체크포인트별 거리 생성
dist = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        dist[i][j] = abs(cp[i][0] - cp[j][0]) + abs(cp[i][1] - cp[j][1])
# print(np.array(dist))

dp = [[999999999999 for _ in range(N)] for _ in range(K + 1)]
dp[0][0] = 0

# 건너뛸 체크포인트가 없는 경우 채우기
for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + dist[i - 1][i]

# 건너뛸 체크포인트가 K개인 만큼 채우기
for i in range(1, K + 1):
    # 건너뛰지 못하는 구간
    dp[i][0], dp[i][1] = 0, dp[i - 1][1]
    dp[i][i] = dist[0][i]
    # print(np.array(dp))
    for j in range(1, N):
        for k in range(i, 0, -1):
            if j - k - 1 < 0:
                continue
            dp[i][j] = min(dp[i][j], dp[i - k][j - k - 1] + dist[j][j - k - 1], dp[i][j - 1] + dist[j - 1][j])
# print(np.array(dp))

print(dp[K][N-1])