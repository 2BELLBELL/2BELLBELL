import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    global cnt
    q = deque()
    q.append((v, 10**9))
    visited = [False] * (N + 1)
    visited[v] = True
    while q:
        node, dist = q.popleft()
        for i in graph[node]:
            if not visited[i[0]]:
                if i[1] < k:
                    visited[i[0]] = True
                else:
                    visited[i[0]] = True
                    cnt += 1
                    q.append([i[0], min(dist, i[1])])


N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

for _ in range(Q):
    k, v = map(int, input().split())
    cnt = 0
    bfs()
    print(cnt)