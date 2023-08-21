from collections import deque

F, S, G, U, D = map(int, input().split())
arr = [None] * (F+1)

q = deque([S])
arr[S] = 0
flag = True

while q:
    tmp = q.popleft()
    if tmp == G:
        print(arr[tmp])
        flag = False
        break
    if tmp + U <= F and arr[tmp + U] == None:
        q.append(tmp + U)
        arr[tmp + U] = arr[tmp] + 1
    if tmp - D >= 1 and arr[tmp - D] == None:
        q.append(tmp - D)
        arr[tmp - D] = arr[tmp] + 1

if flag:
    print('use the stairs')

