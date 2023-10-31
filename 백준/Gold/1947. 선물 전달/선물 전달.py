'''
6 = 265
5 = 44

(dp[i-1] + dp[i-2]) * i
4 = 9
3 = 2
2 = 1
'''

N = int(input())
dp = [0] * (N + 1)
if N == 2:
    print(1)
    exit()
elif N == 1:
    print(0)
    exit()

dp[1] = 0
dp[2] = 1

for i in range(3, N + 1):
    dp[i] = ((dp[i-1] + dp[i-2]) * (i - 1)) % 1000000000

print(dp[N])