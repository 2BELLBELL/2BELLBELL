import sys

N, M = map(int, sys.stdin.readline().split())

# 바닥 장식 모양
deco = []
for i in range(1, N + 1):
    deco.append(list(sys.stdin.readline().strip()))

# 방문 여부 확인용 리스트
visit = []
temp = [False] * M
for i in range(N):
    visit.append(temp[:])

# DFS 함수 생성
def dfs(x, y):
    # 해당 노드 방문 처리
    visit[x][y] = True

    # 해당 노드가 '-'고 옆에도 같은 노드면 옆 노드에서 재귀함수 호출
    if deco[x][y] == '-' and y + 1 < M and deco[x][y + 1] == '-':
        dfs(x, y + 1)
    # 해당 노드가 '|'고 그 아래도 같은 노드면 아래 노드에서 재귀함수 호출
    elif deco[x][y] == '|' and x + 1 < N and deco[x + 1][y] == '|':
        dfs(x + 1, y)
    else:
        return

    
# 방문여부가 False인 좌표를 돌며 재귀 함수가 호출된 만큼 카운팅
cnt = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == False:
            dfs(i, j)
            cnt += 1

print(cnt)