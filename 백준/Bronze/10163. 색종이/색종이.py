import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
idx = [0] * (N + 1)
for k in range(1, N + 1):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x1 + x2):
        for j in range(y1, y1 + y2):
            arr[i][j] = k


for i in range(1001):
    for j in range(1001):
        idx[arr[i][j]] += 1

for i in range(1, N + 1):
    print(idx[i])