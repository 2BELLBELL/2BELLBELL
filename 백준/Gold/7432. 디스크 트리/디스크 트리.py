import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = []
for _ in range(N):
    directory = list(input().rstrip().split('\\'))
    array.append(directory)
array.sort()
# print(array)

for i in range(len(array[0])):
    print(' ' * i + array[0][i])
for i in range(1, N):
    cnt = -1
    # 이전 디렉토리의 부모와 어디까지 겹치는지 체크
    for j in range(len(array[i])):
        if len(array[i - 1]) <= j or array[i - 1][j] != array[i][j]:
            break
        else:
            cnt = j
    # 동일한 디렉토리가 아닌 경우만큼 띄고 시작
    for k in range(cnt + 1, len(array[i])):
        print(' ' * k + array[i][k])
