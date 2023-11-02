import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append((n, 0))
    visited = [True] + [False] * N
    visited[n] = True
    cnt = 0

    while q:
        tmp_n, tmp_cnt = q.popleft()
        for i in members[tmp_n]:
            if not visited[i]:
                visited[i] = True
                q.append((i, tmp_cnt + 1))

    if visited.count(False) == 0:
        return tmp_cnt


N = int(input())
members = [[] for _ in range(N + 1)]
fames = [0] * (N + 1)
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    members[a].append(b)
    members[b].append(a)


max_fame = 9999999999
best_member = []

for i in range(1, N + 1):
    fames[i] = bfs(i)
    if fames[i] < max_fame:
        max_fame = fames[i]
        best_member.clear()
        best_member.append(i)
    elif fames[i] == max_fame:
        best_member.append(i)

print(max_fame, len(best_member))
print(*best_member)