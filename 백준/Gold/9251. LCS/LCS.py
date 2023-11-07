s1 = '?' + input()
s2 = '?' + input()
dp = [[0] * len(s2) for _ in range(len(s1))]
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

# print(np.array(dp))

max_cnt = 0
for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if dp[j][i] > max_cnt:
            max_cnt += 1

print(max_cnt)
