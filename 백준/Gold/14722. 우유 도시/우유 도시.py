import copy
import sys
input = sys.stdin.readline


'''
순서 : 딸 > 초 > 바 > 딸 > ...
동선 : (1, 1)에서 출발해서 (N, N)까지 동쪽 or 남쪽
0: 딸기
1: 초코
2: 바나나
'''
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# # 현재까지의 총 마신 우유
# dp[0][0] = [1, True]
#
# # 0번째 열, 행
# for i in range(1, N):
#     if dp[0][i - 1][1] == True and arr[0][i] != 0 and arr[0][i] - 1 == arr[0][i - 1]:
#         dp[0][i] = [dp[0][i - 1][0] + 1, True]
#     elif dp[0][i - 1][1] == True and arr[0][i] == 0 and arr[0][i] + 2 == arr[0][i - 1]:
#         dp[0][i] = [dp[0][i - 1][0] + 1, True]
#     if dp[i - 1][0][1] == True and arr[i][0] != 0 and arr[i][0] - 1 == arr[i - 1][0]:
#         dp[i][0] = [dp[i - 1][0][0] + 1, True]
#     elif dp[i - 1][0][1] == True and arr[i][0] == 0 and arr[i][0] + 2 == arr[i - 1][0]:
#         dp[i][0] = [dp[i - 1][0][0] + 1, True]

# # 그 외 dp 채우기
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         left = False
#         up = False
#         if dp[i][j - 1][1] == True and arr[i][j] != 0 and arr[i][j] - 1 == arr[i][j - 1]:
#             left = True
#         elif dp[i][j - 1][1] == True and arr[i][j] == 0 and arr[i][j] + 2 == arr[i][j - 1]:
#             left = True
#         if dp[i - 1][j][1] == True and arr[i][j] != 0 and arr[i][j] - 1 == arr[i - 1][j]:
#             up = True
#         elif dp[i - 1][j][1] == True and arr[i][j] == 0 and arr[i][j] + 2 == arr[i - 1][j]:
#             up = True
#
#         print(i, j)
#         print(left, up)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if dp[i][j] % 3 == arr[i - 1][j - 1]:
            dp[i][j] += 1
print(dp[N][N])