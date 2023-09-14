import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    # x가 0인 경우
    if x == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    # x가 자연수인 경우
    else:
        heapq.heappush(arr, x)