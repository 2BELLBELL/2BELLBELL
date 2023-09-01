N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = list(reversed(sorted(B)))
A.sort()
cnt = 0

for i in range(N):
    cnt += A[i] * B[i]

print(cnt)