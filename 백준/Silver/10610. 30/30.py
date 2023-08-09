import sys

N = sorted(list(map(int, sys.stdin.readline().rstrip())))
N.reverse()
total = 0

for i in N:
    total += i

# 각 자리수의 합이 3의 배수면서 N에 0이 없으면 최대로 큰 수 출력
if total % 3 == 0 and 0 in N:
    print(''.join(map(str, N)))
else:
    print(-1)