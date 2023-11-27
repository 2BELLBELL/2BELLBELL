N = int(input())
arr = list(sorted(map(int, input().split())))
l, r = 0, N - 1
answer = []
x = 999999999999999999

while l < r:
    if abs(arr[l] + arr[r]) < x:
        x = abs(arr[l] + arr[r])
        answer = [arr[l], arr[r]]
    if arr[l] + arr[r] < 0:
        l += 1
    else:
        r -= 1

print(*answer)