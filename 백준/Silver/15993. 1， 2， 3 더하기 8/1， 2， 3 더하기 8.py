import sys
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(100001)]
dp[1][1] = dp[2][0] = dp[2][1] = 1
dp[3][0] = dp[3][1] = 2

for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]) % 1000000009
    dp[i][1] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]) % 1000000009

for tmp in arr:
    print(dp[tmp][1], dp[tmp][0])