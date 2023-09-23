def back():
    if len(stack) == M:
        result.add(tuple(stack))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(arr[i])
            back()
            visited[i] = False
            stack.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * N
result = set()
stack = []
back()

for i in list(sorted(result)):
    print(*i)