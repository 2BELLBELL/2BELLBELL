# 현재 경로에서 이어졌으며 안가본 경로가 있으면 방문 표시 후 이동
def dfs(v):
    for i in arr[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

# 가중치가 없는 단방향 그래프 채워넣기
N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            arr[i+1].append(j+1)

# 각 그래프마다 visited 생성 후 dfs 실행
# 인덱스 기준으로 실행하기에 출력시에는 1열부터 출력 
for i in range(1, N+1):
    visited = [0] * (N+1)
    dfs(i)
    print(*visited[1:])