import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for _ in range(N):
    arr = list(input().rstrip())
    stack = []
    cnt = -1
    for i in range(M):
        if stack:
            if arr[i] == 'c':
                cnt = 0
            else:
                cnt += 1
        else:
            if arr[i] == 'c':
                stack.append(arr[i])
                cnt = 0
        print(cnt, end=' ')
    print()