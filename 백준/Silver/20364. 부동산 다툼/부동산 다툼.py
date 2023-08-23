N, Q = map(int, input().split())
duck = [int(input()) for _ in range(Q)]
arr = list(range(0, N+1))

for i in duck:
    tmp = i
    stack = []
    while tmp != 0:
        if arr[tmp] != None:
            tmp //= 2
        elif arr[tmp] == None:
            stack.append(tmp)
            tmp //= 2
    if not stack:
        print(0)
        arr[i] = None
    else:
        print(stack.pop())