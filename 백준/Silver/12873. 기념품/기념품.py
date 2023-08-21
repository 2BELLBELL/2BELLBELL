from collections import deque

N = int(input())
arr = deque(list(range(1, N+1)))
num = 1

while len(arr) != 1:
    arr.rotate(-num**3 + 1)
    arr.popleft()
    num += 1

print(*arr)
