from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    while q:
        computer = q.popleft()
        for i in arr[computer]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return visited.count(True)

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
visited2 = [False] * (N + 1)
# 신뢰하는 컴퓨터 노선 입력
for _ in range(M):
    A, B = map(int, input().split())
    arr[B].append(A)

max_v = 0
max_computer = []
# 각 컴퓨터 별 해킹 가능한 컴퓨터의 수 확인
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    visited[i] = True
    v = bfs(i)
    if v > max_v:
        max_computer.clear()
        max_v = v
        max_computer.append(i)
    elif v == max_v:
        max_computer.append(i)

print(*max_computer)