import sys
from collections import deque

def bfs(v):
    q = deque([v])
    visited = [None] * (N + 1)
    visited[v] = 0
    while q:
        tmp = q.popleft()
        for i in arr[tmp]:
            if visited[i] == None:
                q.append(i)
                visited[i] = visited[tmp] + 1

    return sum(visited[1:])

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
answer = 10**9
answer_idx = 0

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(1, N+1):
    cnt = bfs(i)
    if cnt < answer:
        answer = cnt
        answer_idx = i

print(answer_idx)