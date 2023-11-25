import sys
input = sys.stdin.readline
import heapq

N = int(input().strip())
plus = []
minus = []
for _ in range(N):
    x = int(input().strip())
    if x > 0:
        heapq.heappush(plus, x)
    elif x < 0:
        heapq.heappush(minus, -x)
    else:
        if not plus and not minus:
            print(0)
        elif plus and not minus:
            print(heapq.heappop(plus))
        elif minus and not plus:
            print(-heapq.heappop(minus))
        else:
            if abs(plus[0]) < abs(minus[0]):
                print(heapq.heappop(plus))
            else:
                print(-heapq.heappop(minus))