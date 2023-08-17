N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 해당 집까지 칠할때 필요한 최소 금액
price = [[0] * 3 for _ in range(N)]
# 첫줄은 채워놓기
price[0][0] = arr[0][0]
price[0][1] = arr[0][1]
price[0][2] = arr[0][2]

for i in range(1, N):
    for j in range(3):
        v = 1000000
        for x, y in [[-1, -1], [-1, 1], [-1, 2], [-1, -2]]:
            nx = i+x
            ny = j+y
            if 0 <= nx < N and 0 <= ny < 3 and v > arr[i][j] + price[nx][ny]:
                v = arr[i][j] + price[nx][ny]
        price[i][j] = v

print(min(price[N-1]))