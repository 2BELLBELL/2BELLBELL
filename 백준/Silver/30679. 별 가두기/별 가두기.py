import sys
input = sys.stdin.readline
from collections import deque


def spin(a, b):
    global answer
    q = deque()
    q.append((a, b, 'e', 0))

    while q:
        x, y, dir, cnt = q.popleft()
        if cnt > N * M * 2:
            answer.append(a + 1)
            break
        if dir == 'e' and y + arr[x][y] < M:
            q.append((x, y + arr[x][y], 's', cnt + 1))
        elif dir == 's' and x + arr[x][y] < N:
            q.append((x + arr[x][y], y, 'w', cnt + 1))
        elif dir == 'w' and 0 <= y - arr[x][y]:
            q.append((x, y - arr[x][y], 'n', cnt + 1))
        elif dir == 'n' and 0 <= x - arr[x][y]:
            q.append((x - arr[x][y], y, 'e', cnt + 1))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(N):
    spin(i, 0)

if answer:
    print(len(answer))
    print(*answer)
else:
    print(0)