import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
p_sum = [0] * (N + 1)  # 부분합 리스트 (단, M으로 나눈 나머지로 저장)

# count[idx]는 1부터 x까지의 부분합이 담긴
# (정확하는 M으로 나눈 나머지가 담긴)
# p_sum의 원소들 중에, 그 값이 idx인 것의 개수를 의미함
count = [0] * (M + 1)

# p_sum과 count 구하기
for i in range(N):
    p_sum[i + 1] = (p_sum[i] + arr[i]) % M
    count[p_sum[i + 1]] += 1

# 1부터 x까지의 부분합을 M으로 나눈 나머지가 0이라면,
# 그 부분합 자체로 하나를 카운팅해줘야됨
ans = count[0]

# 그 외의 부분합들을 처리하는 구문임.
# 만약 어떤 두 부분합(1부터 x까지의)을 M으로 나눈 나머지가 같고
# 각각 1부터 a, b 까지의 부분합이라고 가정하면,
# a+1부터 b까지의 부분합은 M으로 나누어떨어진다.
# 이 부분은 수학적인 논리이므로 잘 생각해보자.
for i in range(M + 1):
    # 뽑는 개수가 2인 combination의 변형식임
    ans += (count[i] * (count[i] - 1)) // 2

print(ans)

# L : 1, 2, 3, 1, 2
# array : 0, 1, 3, 6, 7, 9
# res : 3, 0, 2
# array(누적합) 에서 3으로 나누어 떨어지는 인덱스 : 1, 2, 4
# 1, 2, 4 중 2개를 택하면 택한 모든 구간은 3으로 나누어 떨어짐

# 실패 코드
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
sum_arr = [0] * N
sum_arr[0] = arr[0]
if sum_arr[0] % M == 0:
    cnt += sum_arr[0] // M

for i in range(1, N):
    sum_arr[i] = sum_arr[i-1] + arr[i]
    if arr[i] % M == 0:
        cnt += arr[i] // M

for i in sum_arr:
    if i % M == 0:
        cnt += i // M
print(np.array(sum_arr))
print(cnt)

'''