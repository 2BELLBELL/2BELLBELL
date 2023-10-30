'''
2 5 7 1 3  4  8  6  9  3
0 3 5 9 9 10 14 14 17 20
'''
N = int(input())
scores = list(map(int, input().split()))
dp = [0] * N
dp[0] = 0

for i in range(1, N):
    max_v = 0
    for j in range(i):
        max_v = max(max_v, (dp[j - 1] + max(scores[j:i + 1]) - min(scores[j:i + 1])))
    dp[i] = max_v

print(dp[N - 1])