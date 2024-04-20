import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [1] * (N + 1)

for i in range(M, N + 1):
    dp[i] = (dp[i - 1] + dp[i - M]) % 1000000007

print(dp[N])