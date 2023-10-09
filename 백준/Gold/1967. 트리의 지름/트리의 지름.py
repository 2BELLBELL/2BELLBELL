import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    q = deque()
    q.append((s, 0))
    visited = [False] * (V + 1)
    max_num = s
    max_v = 0
    visited[s] = True

    while q:
        tmp_num, tmp_v = q.popleft()
        if tmp_v > max_v:
            max_v = tmp_v
            max_num = tmp_num
        for i, v in arr[tmp_num]:
            if not visited[i]:
                q.append((i, tmp_v + v))
                visited[i] = True
    return max_num, max_v

V = int(input())
arr = [[] for _ in range(V + 1)]
# 간선, 가중치 순으로 노드 정보 입력 받기
for _ in range(V - 1):
    start, end, dis = map(int, input().split())
    arr[start].append((end, dis))
    arr[end].append((start, dis))

# 1번 정점에서 가장 먼 정점 찾기
tmp_idx, tmp_v = bfs(1)
# 찾은 정점에서 가장 먼 정점 찾기
answer_idx, answer_v = bfs(tmp_idx)
print(answer_v)