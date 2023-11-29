import sys

N = int(input())
array = []
for _ in range(N):
    foods = list(input().split())
    array.append(foods[1:])
array.sort()
# print(array)

for i in range(len(array[0])):
    print('--' * i + array[0][i])
for i in range(1, N):
    cnt = -1
    for j in range(len(array[i])):
        if len(array[i - 1]) <= j or array[i - 1][j] != array[i][j]:
            break
        else:
            cnt = j
    for k in range(cnt + 1, len(array[i])):
        print('--' * k + array[i][k])
        