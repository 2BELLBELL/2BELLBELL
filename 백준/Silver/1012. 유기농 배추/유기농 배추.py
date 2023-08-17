import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    arr[x][y] = 0

    for i, j in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
        nx = x+i
        ny = y+j
        # 벽을 안 넘었다면
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
            dfs(nx, ny)

T = int(sys.stdin.readline().rstrip())

for tc in range(T):
    # 2차원 배열로 생성 후 배추 심기
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        Y, X = map(int, sys.stdin.readline().split())
        arr[X][Y] = 1

    # 배추 지렁이 몇마리 심어야 할지 카운팅
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)