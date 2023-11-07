s1 = '?' + input()
s2 = '?' + input()
dp = [[''] * len(s2) for _ in range(len(s1))]
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + s1[i]
        else:
            if len(dp[i][j - 1]) > len(dp[i - 1][j]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]


# print(np.array(dp))

max_cnt = 0
max_word = ''
for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if len(dp[j][i]) > max_cnt:
            max_cnt += 1
            max_word = dp[j][i]

print(max_cnt)
if max_cnt != 0:
    print(max_word)