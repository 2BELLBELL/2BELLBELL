import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)
    arr.sort()
    stack = []
    for i in arr:
        if not stack:
            stack.append(i[1])
        else:
            if stack[-1] < i[1]:
                N -= 1
            else:
                stack.pop()
                stack.append(i[1])

    print(N)