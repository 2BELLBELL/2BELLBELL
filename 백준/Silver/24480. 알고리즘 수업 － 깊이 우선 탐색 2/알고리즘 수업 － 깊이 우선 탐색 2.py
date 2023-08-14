import sys
sys.setrecursionlimit(10**6)
# dfs 함수 정의
def dfs(v):
    # 현재 노드 방문처리
    visited[v] = True
    result.append(v)
    # 현재 노드와 이어진 간선을 순회한다
    for i in arr[v]:
        # 방문하지 않은 간선이 있다면 재귀 실행
        if visited[i] == False:
            # 방문 순서 체크를 위해 카운트를 1개 증가하며 재귀
            dfs(i)

N, M, R = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 순서를 카운팅하고 넣을 변수
cnt = 1
result = []
result_idx = [0] * (N+1)
# 간선 정보 입력
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

# 정점번호를 오름차순으로 변경
for i in arr:
    i.sort()
    i.reverse()

# 시작 정점에서부터 dfs 실행
dfs(R)

# 방문 순서를 인덱스로 하여 리스트 수정
for i, v in zip(result, range(1, len(result)+1)):
    result_idx[i] = v

for i in range(1, len(result_idx)):
    print(result_idx[i])