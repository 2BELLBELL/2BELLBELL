# 재귀함수
def star(N, x, y):
    if N == 1:
        return

    for i in range(x+N//3, x+N-N//3):
        for j in range(y+N//3, y+N-N//3):
            arr[i][j] = ' '

    for i in range(0+x, N+x, N//3):
        for j in range(0+y, N+y, N//3):
            star(N//3, i, j)


N = int(input())
arr = [['*'] * N for _ in range(N)]
star(N, 0, 0)
for i in arr:
    print(''.join(i))
