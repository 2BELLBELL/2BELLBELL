import sys

# 입력 값 받기
arr = sorted(list(map(int, sys.stdin.readline().split())))

# 가장 긴 변이 다른 두변의 합보다 큰 경우
if arr[2] >= arr[0] + arr[1]:
    print(arr[0] + arr[1] + arr[0] + arr[1] - 1)
else:
    print(sum(arr))