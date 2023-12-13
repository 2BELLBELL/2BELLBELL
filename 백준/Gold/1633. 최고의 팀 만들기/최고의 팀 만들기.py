import sys
input = sys.stdin.readline


'''
30 ~ 100명
흑팀 15명 백팀 15명 출전
흑팀 or 백팀 or Pass

'''

dp = [[0 for _ in range(16)] for _ in range(16)]
while True:
    try:
        abil = list(map(int, input().split()))
        for w in range(15, -1, -1):
            for b in range(15, -1, -1):
                if w != 0 and w - 1 >= 0:
                    dp[w][b] = max(dp[w][b], dp[w - 1][b] + abil[0])
                if b != 0 and b - 1 >= 0:
                    dp[w][b] = max(dp[w][b], dp[w][b - 1] + abil[1])

    except:
        print(dp[15][15])
        break