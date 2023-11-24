import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
students = {}
num = 1
for _ in range(M):
    student = input().strip()
    students[student] = num
    num += 1

result = []
for key, value in students.items():
    result.append([key, value])
result.sort(key=lambda x:x[1])

cnt = N
if N >= len(result):
    cnt = len(result)

for i in range(cnt):
    print(result[i][0])