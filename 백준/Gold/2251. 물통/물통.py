import sys
input = sys.stdin.readline
from collections import deque


def move_water():
    visited = set()
    q = deque()
    q.append((0, 0, C))
    answer = set()

    while q:
        x, y, z = q.popleft()
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        if x == 0:
            answer.add(z)
        # A > B
        if x != 0:
            if x + y <= B:
                q.append((0, x + y, z))
            else:
                q.append((x + y - B, B, z))
        # A > C
            if x + z <= C:
                q.append((0, y, x + z))
            else:
                q.append((x + y - C, y, C))
        # B > A
        if y != 0:
            if x + y <= A:
                q.append((x + y, 0, z))
            else:
                q.append((A, x + y - A, z))
        # B > C
            if y + z <= C:
                q.append((x, 0, y + z))
            else:
                q.append((x, y + z - C, C))
        # C > A
        if z != 0:
            if x + z <= A:
                q.append((x + z, y, 0))
            else:
                q.append((A, y, x + z - A))
        # C > B
            if y + z <= B:
                q.append((x, y + z, 0))
            else:
                q.append((x, B, y + z - B))
    return answer

A, B, C = map(int, input().split())
result = list(sorted(move_water()))
print(*result)
