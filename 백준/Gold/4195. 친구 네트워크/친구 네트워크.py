import sys
input = sys.stdin.readline

def find(name):
    # 새로운 친구가 들어온 경우
    if name not in names.keys():
        names[name] = name
        cnt[name] = 1
    # 이미 친구관계가 있고, 대표 친구가 아닌 경우 대표 친구를 찾으러 재귀 (키&값이 다른 경우)
    elif names[name] != name:
        names[name] = find(names[name])
    # 대표 친구를 반환
    return names[name]


def union(x, y):
    x = find(x)
    y = find(y)
    # 대표 친구가 같은 친구가 아니라면 합치고, 친구의 수를 출력
    if x != y:
        names[y] = x
        cnt[x] += cnt[y]
    print(cnt[x])


T = int(input())
for tc in range(1, T + 1):
    F = int(input())
    names = {}
    cnt = {}

    for _ in range(F):
        x, y = input().split()
        union(x, y)