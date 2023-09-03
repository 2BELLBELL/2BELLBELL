N = int(input())
dp = [0] * N
wine = [0] * N
for i in range(N):
    wine[i] = int(input())
dp[0] = wine[0]
if N == 1:
    print(dp[0])
    exit()
dp[1] = wine[0] + wine[1]

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

if N < 3:
    print(dp[N - 1])
else:
    print(dp[N - 1])