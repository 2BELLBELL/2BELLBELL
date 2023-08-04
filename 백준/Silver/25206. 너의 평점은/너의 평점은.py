import sys

# 학점
score = 0
# 과목 평점
my_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
            }

# 학점의 총합
score_total = 0

# P 계산는 제외
cnt = 0

# 학생 점수 받을 리스트
student = []

# P 제외 과목 수와 학점의 총합 계산
for i in range(20):
    A, B, C = sys.stdin.readline().split()
    B = float(B)
    if C != 'P':
        student.append([A, B, C])
        cnt += 1
        score_total += B

sum_score = 0
for i in student:
    sum_score += i[1] * my_dict[i[2]]

print(sum_score/score_total)
