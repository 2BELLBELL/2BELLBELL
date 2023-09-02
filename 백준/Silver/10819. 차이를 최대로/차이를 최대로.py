def back():
    global result
    if len(stack) == N:
        cnt = 0
        for i in range(N - 1):
            cnt += abs(stack[i] - stack[i + 1])
        result = max(cnt, result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(arr[i])
            back()
            visited[i] = False
            stack.pop()

N = int(input())
arr = list(map(int, input().split()))
visited = [False] * N
stack = []
result = 0
back()
print(result)