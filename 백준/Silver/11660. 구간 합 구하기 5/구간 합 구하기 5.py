import sys
input = sys.stdin.readline

# 누적합 구하기
def prefix_sum(n, m):
    prefixSum = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]
    return prefixSum

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
prefixSum = prefix_sum(N, N)

# 부분합 구하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefixSum[x2][y2] - prefixSum[x1-1][y2] - prefixSum[x2][y1-1] + prefixSum[x1-1][y1-1])

# https://code-angie.tistory.com/22