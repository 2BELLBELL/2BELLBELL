n = int(input())
arr = list(map(int, input().split()))
dp = [[1] * n for _ in range(n)]
answer = 1

for i in range(n):
    for j in range(i, n):
        if i == j and i != 0:
            dp[i][j] = dp[i - 1][j]
        else:
            if arr[j] > arr[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i][i] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
        answer = max(answer, dp[i][j])

print(answer)