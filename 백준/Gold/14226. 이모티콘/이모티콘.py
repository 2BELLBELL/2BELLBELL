import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    answer = 0
    q.append((1, 0))
    visited = [[0] * 1001 for _ in range(1001)]

    while q:
        cnt, clipboard = q.popleft()
        if cnt == S:
            answer = visited[cnt][clipboard]
            break

        for i, j in [[cnt, cnt], [cnt + clipboard, clipboard], [cnt - 1, clipboard]]:
            if 0 <= i < 1001 and 0 <= j < 1001 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = visited[cnt][clipboard] + 1

    return answer


S = int(input())
print(bfs())