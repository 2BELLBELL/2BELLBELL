import sys
input = sys.stdin.readline

'''
- dfs 로 방문처리가 안 된 모든 정점을 확인하여 visited 방문 처리
- dfs 시작한 정점 한개당 트리 1개 추가
- dfs 도중 첫 정점과 이어진다면 트리가 아님

Case 1: A forest of 3 trees.
[[], [2], [1, 3], [2, 4], [3], [], []]
1 - 2 - 3 - 4 
5
6

Case 2: There is one tree.
[[], [2], [1, 3], [2, 4], [3, 5], [4, 6], [5]]
1 - 2 - 3 - 4 - 5 - 6

Case 3: No trees.
[[], [2, 3], [1, 3], [2, 1], [5, 6], [4, 6], [5, 4]]
    1           4
  /   \       /   \ 
 2  ㅡ  3    5  ㅡ  6
'''

def dfs(yet, now):
    # 해당 정점과 연결된 미방문 정점을 방문한다
    for i in adj[now]:
        # 단 바로 이전에 방문한 정점은 예외
        if not visited[i] and yet != i:
            visited[i] = True
            dfs(now, i)
        # 이미 연결된 정점을 발견했다면 트리가 아니다.
        else:
            # 단 바로 이전에 방문한 정점은 예외
            if yet != i:
                global flag
                flag = False

case = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    # 간선 정보 입력 받기
    for _ in range(m):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    # 트리의 개수
    tree_cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            flag = True
            dfs(0, i)
            # 트리 여부에 체크
            if flag:
                tree_cnt += 1

    if tree_cnt >= 2:
        print(f'Case {case}: A forest of {tree_cnt} trees.')
    elif tree_cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')

    case += 1