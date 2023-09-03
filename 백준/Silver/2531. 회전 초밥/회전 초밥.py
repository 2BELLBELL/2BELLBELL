N, d, k, c = map(int, input().split())
dic = {c: 1}
arr = [int(input()) for _ in range(N)]
for i in range(k - 1):
    arr.append(arr[i])

result = 0
for i in range(N + k - 1):
    if i < k:
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    else:
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
        if dic[arr[i - k]] == 1:
            del dic[arr[i - k]]
        else:
            dic[arr[i - k]] -= 1
    result = max(result, len(dic.keys()))
print(result)