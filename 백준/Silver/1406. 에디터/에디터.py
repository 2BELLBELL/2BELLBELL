import sys
from collections import deque

left = deque(sys.stdin.readline().strip())
right = deque()
M = int(sys.stdin.readline())

for i in range(M):
    order = sys.stdin.readline().split()
    if order[0] == 'P':
        left.append(order[1])
    if len(left) != 0 and order[0] == 'L':
        right.appendleft(left.pop())
    if len(right) != 0 and order[0] == 'D':
        left.append(right.popleft())
    if len(left) != 0 and order[0] == 'B':
        left.pop()

print(*left, sep='', end='')
print(*right, sep='')
