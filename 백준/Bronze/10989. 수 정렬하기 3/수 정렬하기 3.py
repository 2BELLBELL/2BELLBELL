import sys

# 수의 개수
N = int(sys.stdin.readline())

# 카운팅 정렬을 위한 리스트 생성
arr = [0] * 10001

# arr 의 각 인덱스에 숫자 삽입
for i in range(N):
    arr[int(sys.stdin.readline())] += 1

# 카운팅 정렬된 배열 확인
for i in range(10001):
    # 해당 인덱스에 1 이상이 포함되어 있다면
    if arr[i] >= 1:
        # 해당 숫자만큼 반복해서 출력
        cnt = arr[i]
        for j in range(cnt):
            print(i)
