# 첫번째 입력 값과 두번째 입력 값을 각각의 리스트에 삽입
first = []
second = []
for i in range(3):
    A, B = map(int, input().split())
    first.append(A)
    second.append(B)

# 계수 정렬을 통해 각각의 리스트에서 1개인 값을 출력
first_list = [0]*1001
second_list = [0]*1001

for i in first:
    first_list[i] += 1

for j in second:
    second_list[j] += 1

print(first_list.index(1), second_list.index(1))