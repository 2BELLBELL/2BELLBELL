import sys
input = sys.stdin.readline

'''
0 = 0
1 = 1       1
2 = 1       2
3 = 3       12 21 3
4 = 3       121 13 31
5 = 4       131 212 23 32 
6 = 8       123 1212 132 2121 213 231 312 321  
'''

dp = [[0, 0, 0] for _ in range(100001)]
dp[1], dp[2], dp[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]
for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % 1000000009)