import sys
input = sys.stdin.readline


def find(target):
    if target != friends[target]:
        friends[target] = find(friends[target])

    return friends[target]


def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 노드 기준으로 합친다
    if arr[a] < arr[b]:
        friends[b] = a
    else:
        friends[a] = b


N, M, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
answer = 0
friends = list(range(N + 1))

for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

cnt = 0
for i in friends:
    if cnt == i:
        answer += arr[i]
    cnt += 1

    if k < answer:
        print('Oh no')
        exit()

print(answer)