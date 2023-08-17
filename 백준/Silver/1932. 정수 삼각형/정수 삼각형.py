import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1):
        v = 0
        # 이전 행의 현재 열과 / 이전 열을 더한값을 비교하여 더 큰값으로 갱신
        for x, y in [[-1, 0], [-1, -1]]:
            nx = i+x
            ny = j+y
            if 0 <= nx < N and 0 <= ny < i and v < arr[i][j] + arr[nx][ny]:
                v = arr[i][j] + arr[nx][ny]
        arr[i][j] = v

print(max(arr[N-1]))