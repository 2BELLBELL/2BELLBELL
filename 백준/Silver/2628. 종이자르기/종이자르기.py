n, m = map(int, input().split())
cut = int(input())
row = []
col = []
for _ in range(cut):
    a, b = map(int, input().split())
    if a == 0:
        row.append(b)
    elif a == 1:
        col.append(b)
row.sort()
col.sort()

max_x = m
max_y = n
if row:
    if row[0] <= m - row[-1]:
        max_x = m - row[-1]
    else:
        max_x = row[0]
    for i in range(len(row)-1, 0, -1):
        if row[i] - row[i-1] > max_x:
            max_x = row[i] - row[i-1]
if col:
    if col[0] <= n - col[-1]:
        max_y = n - col[-1]
    else:
        max_y = col[0]
    for i in range(len(col)-1, 0, -1):
        if col[i] - col[i-1] > max_y:
            max_y = col[i] - col[i-1]


print(max_x * max_y)