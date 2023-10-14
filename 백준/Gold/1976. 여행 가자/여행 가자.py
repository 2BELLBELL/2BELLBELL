import sys
input = sys.stdin.readline


# find 연산
def find(target):
    # 본인이 집합의 대표가 아니라면
    # 집합의 대표와  같은 숫자로 변경되도록 재귀
    if target != citys[target]:
        citys[target] = find(citys[target])

    # 집합의 대표를 반환
    return citys[target]


# union 연산
def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 노드 기준으로 합친다
    if a < b:
        citys[b] = a
    else:
        citys[a] = b


N = int(input())
M = int(input())
citys = list(range(N))
for i in range(N):
    city = list(map(int, input().split()))
    for j in range(N):
        if city[j] == 1:
            # 유니온
            union(i, j)

travle = list(map(int, input().split()))
result = citys[travle[0] - 1]
for i in range(1, M):
    if citys[travle[i] - 1] != result:
        print('NO')
        exit()
print('YES')