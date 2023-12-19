import sys
input = sys.stdin.readline
import math


def make_seg(idx, s, e):
    if s == e:
        seg[idx] = [arr[s], s]
        return seg[idx]

    mid = (s + e) // 2
    make_seg(idx * 2, s, mid)
    make_seg(idx * 2 + 1, mid + 1 , e)

    smaller_index = idx * 2
    if seg[idx * 2][0] > seg[idx * 2 + 1][0]:
        smaller_index = idx * 2 + 1
    seg[idx] = [seg[smaller_index][0], seg[smaller_index][1]]


def update(index, left, right, start, end, value):
  if right < start or end < left:
      return
  if left == right:
      seg[index] = [value, left]
      return

  mid = (left + right) // 2
  update(index*2, left, mid, start, end, value)
  update(index*2+1, mid+1, right, start, end, value)

  smaller_index = index*2
  if seg[index*2][0] > seg[index*2+1][0]:
    smaller_index = index*2+1

  seg[index] = [seg[smaller_index][0], seg[smaller_index][1]]

N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())

# 트리의 최대 층 수
max_size = 2 ** (math.ceil(math.log2(N)) + 1)

# 세그먼트 트리 생성
seg = [[0, 0]] * max_size
make_seg(1, 1, N)


for _ in range(M):
    tmp = list(map(int, input().split()))

    if tmp[0] == 2:
        print(seg[1][1])
    else:
        update(1, 1, N, tmp[1], tmp[1], tmp[2])