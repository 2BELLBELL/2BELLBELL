import sys
input = sys.stdin.readline


n, m = map(int, input().split())
k = int(input())
blocked = set()
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1

for _ in range(k):
    a, b, c, d = map(int, input().split())
    blocked.add((a, b, c, d))
    blocked.add((c, d, a, b))

for i in range(n + 1):
    for j in range(m + 1):
        if i < n and (i + 1, j, i, j) not in blocked and (i, j, i + 1, j) not in blocked:
            dp[i + 1][j] += dp[i][j]
        if j < m and (i, j + 1, i, j) not in blocked and (i, j, i, j + 1) not in blocked:
            dp[i][j + 1] += dp[i][j]

print(dp[n][m])