N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
dp[N-1][N-1] = 0

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        if dp[i][j] >= 1:
            if arr[i][j] + i < N:
                dp[arr[i][j] + i][j] += dp[i][j]
            if arr[i][j] + j < N:
                dp[i][arr[i][j] + j] += dp[i][j]

print(dp[N-1][N-1])