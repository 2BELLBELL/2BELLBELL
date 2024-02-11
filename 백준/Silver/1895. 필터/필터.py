import sys
input = sys.stdin.readline


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
T = int(input())
answer = 0

for x in range(R - 2):
    for y in range(C - 2):
        f = []
        for nx in range(x, x + 3):
            for ny in range(y, y + 3):
                f.append(arr[nx][ny])

        f.sort()
        if f[len(f) // 2] >= T:
            answer += 1

print(answer)