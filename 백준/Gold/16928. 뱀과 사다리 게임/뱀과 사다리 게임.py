from collections import deque

N, M = map(int, input().split())
visited = [-1] * 101
# 지름길 딕셔너리 생성
dic = {}
for i in range(N + M):
    start, end = map(int, input().split())
    dic[start] = end

# 1에서부터 시작
q = deque([1])
visited[1] = 0

# BFS 실행
while q:
    tmp = q.popleft()
    # 지름길에 도착한 경우
    if tmp in dic:
        # 지름길의 최소 횟수를 현재 위치의 최소 횟수와 동일하게 맞춘다
        visited[dic[tmp]] = visited[tmp]
        # 현재 위치를 지름길을 이동한 위치로 변경한다
        tmp = dic[tmp]
    # 100번째에 도착하는 순간 중지
    if tmp == 100:
        break
    # 주사위 1 ~ 6까지 던져서 100이하이면서 이동하지 않은곳이면 방문처리, 큐에 추가
    for i in range(1, 7):
        if tmp + i <= 100 and visited[tmp + i] == -1:
            visited[tmp + i] = visited[tmp] + 1
            q.append(tmp + i)

# 100번째 땅에 가는 최소 횟수 출력
print(visited[100])