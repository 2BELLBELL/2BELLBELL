import sys
from collections import deque
input = sys.stdin.readline

# 여행 갈 수 있는 지역 체크
def bfs(v):
    q = deque([v])
    visited = [False] * N
    visited[v] = True
    while q:
        tmp = q.popleft()
        for i in arr[tmp]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return visited

N = int(input())
M = int(input())
arr = [[] for _ in range(N)]

# 도시 사이의 길 체크하기
for i in range(N):
    city = list(map(int, input().split()))
    for j in range(N):
        if city[j] == 1:
            arr[i].append(j)
plan = list(map(int, input().split()))

# 첫번째 도시로부터 갈 수 있는 모든 곳을 체크
result = bfs(plan[0] - 1)

# 가능하면 YES
answer = 'YES'
# 여행 계획을 순회하며 갈 수 없는 곳이 있으면 NO로 변경
for i in plan:
    if not result[i - 1]:
        answer = 'NO'
# 가능 여부 출력
print(answer)