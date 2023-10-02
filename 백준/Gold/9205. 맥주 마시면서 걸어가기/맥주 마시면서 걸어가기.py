from collections import deque
def go(x, y):
    q = deque([(x, y)])
    visited = [0 for i in range(n + 1)]
    while q:
        tmp_x, tmp_y = q.popleft()
        if abs(tmp_x - rock[0]) + abs(tmp_y - rock[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                new_x, new_y = cu[i]
                if abs(tmp_x - new_x) + abs(tmp_y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1
    print("sad")
    return

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    home = list(map(int, input().split()))
    cu = [list(map(int, input().split())) for _ in range(n)]
    rock = list(map(int, input().split()))
    go(home[0], home[1])