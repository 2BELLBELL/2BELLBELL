import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y, z):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    elif x == y:
        global answer
        answer += z
    else:
        parent[x] = y


while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    parent = list(range(m))
    roads = []
    answer = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        roads.append([x, y, z])
    # 거리순으로 정렬
    roads.sort(key=lambda x: x[2])

    for road in roads:
        x, y, z = road[0], road[1], road[2]
        union(x, y, z)

    print(answer)