arr = []
for _ in range(9):
    arr.append(int(input()))
# 찾아야하는 키의 합
cnt = sum(arr) - 100

for i in range(8):
    for j in range(i + 1, 9):
        if arr[i] + arr[j] == cnt:
            result = set(arr) - set([arr[i], arr[j]])
            break

result = list(sorted(result))
for i in result:
    print(i)