import sys
input = sys.stdin.readline

N = int(input())
arr = [float(input()) for _ in range(N)]

answer = max(arr)
for i in range(N):
    tmp = arr[i]
    for j in range(i + 1, N):
        tmp *= arr[j]
        answer = max(answer, tmp)

print('%.3f' % answer)