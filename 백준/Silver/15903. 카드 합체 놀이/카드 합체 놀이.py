import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)
for i in range(m):
    A = heapq.heappop(arr)
    B = heapq.heappop(arr)
    heapq.heappush(arr, A + B)
    heapq.heappush(arr, A + B)
print(sum(arr))