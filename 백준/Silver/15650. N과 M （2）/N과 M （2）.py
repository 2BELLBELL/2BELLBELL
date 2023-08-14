def dfs():
    if len(arr) == m+1:
        print(*arr[1:])
        return
    for i in range(1, n+1):
        if i not in arr and max(arr) < i:
            arr.append(i)
            dfs()
            arr.pop()


n, m = map(int, input().split())
arr = [0]

dfs()