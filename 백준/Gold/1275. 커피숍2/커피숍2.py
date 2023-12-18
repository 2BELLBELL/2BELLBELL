import sys
input = sys.stdin.readline
import math


def make_seg(idx, s, e):
    # 리프노드인 경우
    if s == e:
        seg[idx] = arr[s]
        return seg[idx]

    # 아래층으로 재귀
    mid = (s + e) // 2
    left = make_seg(idx * 2, s, mid)
    right = make_seg(idx * 2 + 1, mid + 1, e)

    # 왼쪽 자식 + 오른쪽 자식 넣기
    seg[idx] = left + right
    return seg[idx]


def update(idx, s, e, x, y):
    if s == e == x:
        seg[idx] = y
        return
    if x < s or x > e:
        return
    mid = (s + e) // 2
    update(idx * 2, s, mid, x, y)
    update(idx * 2 + 1, mid + 1, e, x, y)
    seg[idx] = seg[idx * 2] + seg[idx * 2 + 1]

def find(idx, s, e, l, r):
    # 범위 밖일 때
    if r < s or l > e:
        return 0

    # 현재 범위에 들어왔을 때
    if l <= s and e <= r:
        return seg[idx]

    mid = (s + e) // 2
    left = find(idx * 2, s, mid, l, r)
    right = find(idx * 2 + 1, mid + 1, e, l, r)
    return left + right

N, Q = map(int, input().split())
arr = list(map(int, input().split()))


# 트리의 최대 층 수
max_size = 2 ** (math.ceil(math.log2(N)) + 1)

# 세그먼트 트리 생성
seg = [0] * max_size
make_seg(1, 0, len(arr) - 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    # 합부터 출력
    if x <= y:
        print(find(1, 0, N - 1, x - 1, y - 1))
    else:
        print(find(1, 0, N - 1, y - 1, x - 1))
    # a번째 수를 b로 바꾼다
    update(1, 0, N - 1, a - 1, b)

