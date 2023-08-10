import sys
# N과 K의 수를 입력 받는다
N, K = map(int, sys.stdin.readline().split())

# 1부터 N까지의 리스트 생성
N_list = list(range(1, N + 1))
result = []
cnt = K - 1

while len(N_list) != 0:
    if cnt < len(N_list):
        result.append(N_list.pop(cnt))
        cnt += K - 1
    else:
        cnt -= len(N_list)

result = ', '.join(list(map(str, result)))
print(f'<{result}>')
