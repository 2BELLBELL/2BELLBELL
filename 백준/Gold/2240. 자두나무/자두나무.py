import sys
input = sys.stdin.readline


# 초, 이동 가능 횟수
T, W = map(int, input().split())
arr = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]

dp[1][0] = arr[1] % 2
dp[1][1] = arr[1] // 2
for t in range(2, T + 1):
    for w in range(W + 1):
        if w % 2 == 0:
            dp[t][w] = max(dp[t - 1][0:w + 1]) + arr[t] % 2
        else:
            dp[t][w] = max(dp[t - 1][0:w + 1]) + arr[t] // 2
            
print(max(dp[-1]))