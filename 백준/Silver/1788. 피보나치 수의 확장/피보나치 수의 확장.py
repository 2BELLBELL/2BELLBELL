def fibo(x):
    if x == 0:
        return dp[x]
    if x == 1:
        return dp[x]

    for i in range(2, x + 1):
        dp[i] = dp[i - 2] % 1000000000 + dp[i - 1] % 1000000000

    return dp[x] % 1000000000


n = int(input())
dp = [0] * 1000001
dp[0] = 0
dp[1] = 1
if n < 0 and abs(n) % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(fibo(abs(n)))