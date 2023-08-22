import sys

N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
parent = [None] * (N+1)
parent[1] = 0
for _ in range(N-1):
    start, end = map(int, sys.stdin.readline().split())
    arr[start].append(end)
    arr[end].append(start)

S = 1
stack = [1]

while stack:
    for i in arr[S]:
        if parent[i] == None:
            stack.append(S)
            parent[i] = S
            S = i
            break
    else:
        if stack:
            S = stack.pop()
        else:
            break

for i in parent[2:]:
    print(i)