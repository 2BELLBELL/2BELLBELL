N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

# 이전 요소까지 돌며 현재 요소보다 큰 요소 중 제일 큰 요소 + 1 
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))