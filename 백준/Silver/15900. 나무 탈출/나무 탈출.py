import sys
sys.setrecursionlimit(500000) 
input = sys.stdin.readline

def dfs(n):
    visited[n] = True
    for i in arr[n]:
        if visited[i] == False:
            distance[i] = distance[n] + 1
            dfs(i)

N = int(input())
arr = [[] for _ in range(N + 1)]
distance = [0 for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(N-1):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

dfs(1)

for i in range(2, N+1):
    if len(arr[i]) == 1:
        answer += distance[i]

if answer % 2 == 0:
    print('No')
else:
    print('Yes')