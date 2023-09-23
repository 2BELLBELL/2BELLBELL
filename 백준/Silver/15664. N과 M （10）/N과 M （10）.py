def back(num):
    if len(stack) == M:
        result.add(tuple(stack))
        return

    for i in range(num, N):
        if not visited[i]:
            visited[i] = True
            stack.append(arr[i])
            back(i)
            visited[i] = False
            stack.pop()

N, M = map(int, input().split())
arr = list(sorted(map(int, input().split())))
visited = [False] * N
result = set()
stack = []
back(0)

for i in sorted(result):
    print(*i)