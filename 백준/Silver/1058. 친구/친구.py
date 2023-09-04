from collections import deque


def bfs(v):
    q = deque([])
    # 중복 친구 제거용
    visited = [False] * N
    visited[v] = True
    # 최대 친구 수
    max_friends = 0
    # 바로 이어진 친구
    for i in arr[v]:
        q.append([i, 1])
        max_friends += 1
        visited[i] = True

    while q:
        tmp, num = q.popleft()
        for i in arr[tmp]:
            # 중복이 아니며, 친구를 두다리 건너지 않은 경우
            if not visited[i] and num < 2:
                q.append([i, num + 1])
                max_friends += 1
                visited[i] = True
    return max_friends

N = int(input())
arr = [[] for _ in range(N)]
result = 0
for i in range(N):
    word = input()
    for j in range(N):
        if word[j] == 'Y':
            arr[i].append(j)

for i in range(N):
    result = max(bfs(i), result)

print(result)
