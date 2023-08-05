import sys

# 반의 총 학생 수
students = int(sys.stdin.readline())

# 학생 수 만큼 2차원 배열 만들기
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(students)]

stu_dic = {}
for i in range(students):
    stu_dic[i] = []



# 각 열을 순회하며 다음 열과 비교
for i in range(5):
    for j in range(students):
        for k in range(students):
            if arr[j][i] == arr[k][i]:
                if j == k:
                    continue
                else:
                    stu_dic[j].append(k)

for i in range(students):
	stu_dic[i] = set(stu_dic[i])

for i in range(students):
	stu_dic[i] = list(stu_dic[i])

answer_list = []
for i in range(students):
	answer_list.append(len(stu_dic[i]))

leader = max(answer_list)
answer = answer_list.index(leader) + 1
print(answer)