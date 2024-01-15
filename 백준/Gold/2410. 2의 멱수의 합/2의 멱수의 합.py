import sys
input = sys.stdin.readline


'''
2의 제곱의 합
1 = 1
1

2 = 2
1 1
2 

3 = 2
1 1 1
1 2

4 = 4
1 1 1 1
1 1 2
2 2
4

5 = 4
1 1 1 1 1
1 1 1 2
1 2 2
1 4

6 = 6
1 1 1 1 1 1
1 1 1 1 2
1 1 2 2
2 2 2
1 1 4
2 4

'''
N = int(input())
dp = [0] * 1000001
dp[1], dp[2], dp[3], dp[4] = 1, 2, 2, 4

for i in range(3, 1000001):
    if i % 2:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 1] + dp[i // 2]) % 1000000000
print(dp[N])