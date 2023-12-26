N = int(input())
dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
dp[2] = 7

if N <= 2:
    print(dp[N])
    exit()

for i in range(3, N + 1):
    dp[i] = ((dp[i - 1] * 3) + dp[i - 2] - dp[i - 3]) % 1000000007

print(dp[N] % 1000000007)