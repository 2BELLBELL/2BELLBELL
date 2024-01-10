import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    visited = [[False] * (W + 2) for _ in range(H + 2)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    result = 0


    while q:
        x, y = q.popleft()
        if x % 2 == 0:
            for i, j in [[1, 0], [-1, 0], [1, -1], [-1, -1], [0, -1], [0, 1]]:
                nx, ny = x+i, y+j
                if 0 <= nx < H + 2 and 0 <= ny < W + 2 and not visited[nx][ny]:
                    if arr[nx][ny] == 1:
                        result += 1
                    elif arr[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = True
        else:
            for i, j in [[1, 0], [-1, 0], [1, 1], [-1, 1], [0, -1], [0, 1]]:
                nx, ny = x+i, y+j
                if 0 <= nx < H + 2 and 0 <= ny < W + 2 and not visited[nx][ny]:
                    if arr[nx][ny] == 1:
                        result += 1
                    elif arr[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    return result


W, H = map(int, input().split())
arr = [[0] * (W + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(H)] + [[0] * (W + 2)]
print(bfs())
