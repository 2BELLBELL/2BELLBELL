import sys
input = sys.stdin.readline
from collections import deque


while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    arr = list(map(int, input().split()))
    if k == arr[0]:
        print(0)
        continue
    tree = [0] * (arr[-1] + 1)

    temp = deque()
    for i in range(n):
        temp.append(arr[i])
        tree[arr[i]] = temp[0]
        if i != n - 1 and i != 0:
            if arr[i] + 1 != arr[i + 1]:
                temp.popleft()

    nodes = set()
    i, j = tree[k] + -1, tree[k] + 1
    while True:
        flag = False
        if tree[i]:
            nodes.add(i)
            i -= 1
            flag = True
        if tree[j]:
            nodes.add(j)
            j += 1
            flag = True
        if not flag:
            break

    answer = 0

    for i in tree:
        if i in nodes:
            answer += 1

    print(answer)