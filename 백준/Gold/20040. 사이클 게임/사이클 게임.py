import sys
input = sys.stdin.readline

def find(target):
    if target != points[target]:
        points[target] = find(points[target])

    return points[target]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        points[y] = x
    elif x > y:
        points[x] = y
    else:
        print(i + 1)
        exit()

n, m = map(int, input().split())
points = list(range(n))
for i in range(m):
    x, y = map(int, input().split())
    union(x, y)

print(0)