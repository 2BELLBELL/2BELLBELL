N = int(input())
arr = list(map(int, input().split()))
tmp = [1]
for i in range(1, N):
    tmp.insert(i - arr[i], i+1)
print(*tmp)