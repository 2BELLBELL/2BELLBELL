import sys

# 입력 값 생성
arr = sys.stdin.readline().rstrip()
lst = []

for i in range(len(arr)):
    for j in range(len(arr)-i):
        lst.append(arr[j:j+i+1])

print(len(set(lst)))

