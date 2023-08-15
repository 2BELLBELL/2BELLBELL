import sys
from collections import deque

T = int(sys.stdin.readline())

for tc in range(T):
    arr = list(sys.stdin.readline().strip())
    left = deque()
    right = deque()

    for i in arr:
        if len(left) != 0 and i == '<':
            right.appendleft(left.pop())
        elif len(right) != 0 and i == '>':
            left.append(right.popleft())
        elif len(left) != 0 and i == '-':
            left.pop()
        elif i not in ['<', '>', '-']:
            left.append(i)

    print(*left, sep='', end='')
    print(*right, sep='')
