# 마이너스를 기준으로 나눠서 입력 받기
N = input().split('-')

# 각 나눠진 식에서 플러스를 기준으로 다시 나누기
for i in range(len(N)):
    N[i] = list(map(int, N[i].split('+')))

# 첫번째 리스트는 무조건 양수
answer = sum(N[0])
# 이후 나오는 수식은 다 빼준다
for i in range(1, len(N)):
    answer -= sum(N[i])

print(answer)