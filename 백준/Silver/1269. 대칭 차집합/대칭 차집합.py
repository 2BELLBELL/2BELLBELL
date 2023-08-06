import sys
A, B = map(int, sys.stdin.readline().split())

# 두 집합 set로 입력 받기
A_set = set(list(map(int, sys.stdin.readline().split())))
B_set = set(list(map(int, sys.stdin.readline().split())))

# 대칭 차집합의 원소 세기
A_B = A_set.difference(B_set)
B_A = B_set.difference(A_set)
result = len(A_B) + len(B_A)

# 결과 값 출력
print(result)