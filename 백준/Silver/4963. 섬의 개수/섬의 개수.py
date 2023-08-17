import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    arr[x][y] = 0
    # 상하좌우대각선 8방향으로 확인
    for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]:
        nx = x+i
        ny = y+j
        # 벽을 안 넘었다면
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)