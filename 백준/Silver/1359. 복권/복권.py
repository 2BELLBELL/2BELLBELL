import sys
input = sys.stdin.readline
from itertools import combinations, permutations, product

n, m, k = map(int, input().split())

ans = 0
arr = list(combinations(range(n), m))

for combo in arr:
    cnt = 0
    for num in combo:
        if num < m:
            cnt += 1
    if cnt >= k:
        ans += 1

result = ans / len(arr)
print(result)