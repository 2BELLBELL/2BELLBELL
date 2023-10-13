import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# find 연산
def find(target):
    # 본인이 집합의 대표면 바로 반환
    if target == parent[target]:
        return target

    # 경로 압축
    parent[target] = find(parent[target])

    # 집합의 대표가 아닌 경우 대표를 반환
    return parent[target]


# union 연산
def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 노드 기준으로 합친다
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = list(range(n + 1))
for _ in range(m):
    cal, a, b = map(int, input().split())
    # 유니온
    if cal == 0:
        union(a, b)
    # 파인드
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')