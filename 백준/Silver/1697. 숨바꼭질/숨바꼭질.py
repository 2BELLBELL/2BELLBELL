def search(start, end):
    que = [start]
    visited[start] = 1
    while True:
        tmp = que.pop(0)
        if tmp == end:
            return
        if tmp + 1 <= 100000 and visited[tmp+1] == 0:
            que.append(tmp + 1)
            visited[tmp + 1] = visited[tmp] + 1
        if tmp - 1 >= 0 and visited[tmp-1] == 0:
            que.append(tmp - 1)
            visited[tmp - 1] = visited[tmp] + 1
        if tmp * 2 <= 100000 and visited[tmp*2] == 0:
            que.append(tmp * 2)
            visited[tmp * 2] = visited[tmp] + 1


N, K = map(int, input().split())
visited = [0] * 100001
search(N, K)
print(visited[K]-1)