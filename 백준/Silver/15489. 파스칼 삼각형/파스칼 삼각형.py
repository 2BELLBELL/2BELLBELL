R, C, W = map(int, input().split())
dp = [[1] for _ in range(31)]
dp[1] = [1, 1]
for i in range(2, 31):
    tmp = [1]
    for j in range(len(dp[i - 1]) - 1):
        tmp.append(dp[i - 1][j] + dp[i - 1][j + 1])
    tmp.append(1)
    dp[i] = tmp
answer = 0
num = 1
for i in range(R - 1, R + W - 1):
    answer += sum(dp[i][C - 1:C - 1 + num])
    num += 1
print(answer)