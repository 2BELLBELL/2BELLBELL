def back(num):
    if len(stack) == M:
        result.add(tuple(stack))
        return

    for i in range(num, N):
        stack.append(arr[i])
        back(i)
        stack.pop()

N, M = map(int, input().split())
arr = list(sorted(map(int, input().split())))
result = set()
stack = []
back(0)

for i in sorted(result):
    print(*i)