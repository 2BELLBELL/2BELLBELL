def two(n):
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 15746
    return arr[n]

N = int(input())
arr = [0] * (N+2)

print(two(N))