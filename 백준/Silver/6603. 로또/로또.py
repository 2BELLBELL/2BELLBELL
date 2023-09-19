def back():
    if len(stack) == 6:
        return result.add(tuple(sorted(stack)))

    for i in range(k):
        if not visited[i]:
            stack.append(arr[i])
            visited[i] = True
            back()
            stack.pop()
            visited[i] = False

while True:
    case = list(map(int, input().split()))
    if case[0] == 0:
        break
    k = case[0]
    arr = case[1:]
    visited = [False] * k
    stack = []
    result = set()
    back()
    for i in sorted(result):
        print(*i)
    print()