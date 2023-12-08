'''
k = 1
answer = 1

k = 2
answer = n + 1

k = 3
answer = N이 1 낮은 dp + K가 1 낮은 dp

6 1인 경우 = 1개
6

6 2인 경우 = N + 1개 (7개)
0 6
1 5
2 4
3 3
4 2
5 1
6 0

6 3인 경우 = 28개
(N이 6이고 K가 2인 ...7개)
0 0 6
0 1 5
0 2 4
0 3 3
0 4 2
0 5 1
0 6 0
(N이 5이고 K가 2인 ...6개)
1 0 5
1 1 4
1 2 3
1 3 2
1 4 1
1 5 0
(N이 1... K가 2인?)
2차원 배열로 만들어서 더해가는 식으로

'''
N, K = map(int, input().split())

# K가 1일때 반례
if K == 1:
    print(1)
    exit()
    
dp = [[0] * (N + 1) for _ in range(K + 1)]
# 모든 열의 1, 2 행은 1과 N + 1개로 고정
for i in range(1, N + 1):
    dp[1][i], dp[2][i] = 1, i + 1

for i in range(1, K + 1):
    dp[i][1] = i
    for j in range(2, N + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

# print(np.array(dp))
print(dp[K][N])