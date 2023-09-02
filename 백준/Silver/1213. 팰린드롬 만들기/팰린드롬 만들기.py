word = list(map(ord, list(input())))
arr = [0] * 27
for i in word:
    arr[i-65] += 1

cnt = 0
total = 0
for i in arr:
    if i % 2 == 1:
        cnt += 1

if (len(word) % 2 == 0 and cnt >= 1) or (len(word) % 2 == 1 and cnt != 1):
    print("I'm Sorry Hansoo")
else:
    result = ''
    mid = ''
    for i in range(27):
        if arr[i] % 2 == 0:
            tmp = arr[i]
            while tmp // 2 != arr[i]:
                result += chr(i + 65)
                arr[i] -= 1
        else:
            mid = chr(i + 65)
            arr[i] -= 1
            tmp = arr[i]
            while tmp // 2 != arr[i]:
                result += chr(i + 65)
                arr[i] -= 1
    result += mid
    for i in range(26, -1, -1):
        tmp = arr[i]
        while tmp != 0:
            result += chr(i + 65)
            tmp -= 1
    print(result)