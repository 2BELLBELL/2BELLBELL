import sys
input = sys.stdin.readline


n, m = map(int, input().split())
stack = []
for _ in range(n):
    p, l = map(int, input().split())
    mailliji = list(sorted(map(int, input().split())))
    if p > l:
        stack.append(mailliji[p - l])
    elif p == l:
        stack.append(mailliji[0])
    elif p < l:
        stack.append(1)
stack.sort()
cnt = 0
for i in stack:
    if m >= i:
        m -= i
        cnt += 1
    else:
        print(cnt)
        exit()
print(cnt)