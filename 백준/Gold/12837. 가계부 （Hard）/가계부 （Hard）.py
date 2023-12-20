import sys
input = sys.stdin.readline
import math


def update(idx, s, e, x, y):
    if x < s or x > e:
        return
    if s == e:
        seg[idx] += y
        return

    mid = (s + e) // 2
    update(idx * 2, s, mid, x, y)
    update(idx * 2 + 1, mid + 1, e, x, y)

    seg[idx] = seg[idx * 2] + seg[idx * 2 + 1]

def find(idx, s, e, x, y):
    # 범위 밖일 때
    if y < s or x > e:
        return 0

    # 현재 범위에 들어왔을 때
    if x <= s and e <= y:
        return seg[idx]

    mid = (s + e) // 2
    left = find(idx * 2, s, mid, x, y)
    right = find(idx * 2 + 1, mid + 1, e, x, y)
    return left + right

N, Q = map(int, input().split())

# 트리의 최대 층 수
max_size = 2 ** (math.ceil(math.log2(N)) + 1)

# 세그먼트 트리 생성
seg = [0] * max_size

for _ in range(Q):
    order, x, y = list(map(int, input().split()))

    if order == 1:
        update(1, 0, N - 1, x - 1, y)
    else:
        print(find(1, 0, N - 1, x - 1, y - 1))