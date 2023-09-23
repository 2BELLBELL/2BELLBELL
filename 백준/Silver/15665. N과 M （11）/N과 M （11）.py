def back():
    if len(stack) == M:
        result.add(tuple(stack))
        return

    for i in range(N):
        stack.append(arr[i])
        back()
        stack.pop()

N, M = map(int, input().split())
arr = list(sorted(map(int, input().split())))
result = set()
stack = []
back()

for i in sorted(result):
    print(*i)