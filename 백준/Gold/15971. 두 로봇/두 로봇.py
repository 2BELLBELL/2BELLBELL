from collections import deque

## 나중에 다시풀기
def bfs():
  queue = deque()
  queue.append((b, 0))
  dp[b] = 0

  while queue:
    t, v = queue.popleft()

    for x in graph[t]:
      if dp[x[0]] == -1:
        dp[x[0]] = v + x[1]
        queue.append((x[0], dp[x[0]]))

def dfs(a):
  global answer
  stack = []
  stack.append((a, 0, 0))
  visited = [False] * (n + 1)
  visited[a] = True
  while stack:
    t, v, max_len = stack.pop()
    answer = min(answer, v + dp[t] - max_len)
      
    for x in graph[t]:
      if not visited[x[0]]:
        n_len = max(max_len, x[1])
        stack.append((x[0], v + x[1], n_len))
        visited[x[0]] = True
    
n, a, b = map(int, input().split())
if n == 1 or a == b:
  print(0)
  exit(0)

graph = [[] for _ in range(n + 1)]
dp = [-1] * (n + 1)
answer = float('inf')
for _ in range(1, n):
  x, y, v = map(int, input().split())
  graph[x].append((y, v))
  graph[y].append((x, v))
bfs()
dfs(a)
print(answer)