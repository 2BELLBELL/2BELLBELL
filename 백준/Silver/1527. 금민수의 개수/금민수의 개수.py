import sys
input = sys.stdin.readline
from itertools import product

A, B = map(int, input().split())
answer = 0

for i in range(len(str(A)), len(str(B)) + 1):
    for j in product([4, 7], repeat=i):
        if A <= int(''.join(map(str, j))) <= B:
            answer += 1
print(answer)