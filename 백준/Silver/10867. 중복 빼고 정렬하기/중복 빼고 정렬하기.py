import sys

# 입력 값 받기
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 카운팅 정렬
cnt_sort = [0] * 2001

# 정렬 내 숫자 채우기
for i in arr:
    cnt_sort[i+1000] += 1

# 개수가 0이 아니면 출력
for i in range(2001):
    if cnt_sort[i] != 0:
        print(i-1000, end=' ')

