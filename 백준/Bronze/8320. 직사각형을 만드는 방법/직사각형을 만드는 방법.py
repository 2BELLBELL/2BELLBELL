n = int(input())
cnt = n
for i in range(2, int(n**0.5)+1):
    for j in range(i**2, n+1, i):
        cnt += 1
print(cnt)