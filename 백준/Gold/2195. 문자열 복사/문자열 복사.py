s = input()
p = input()
cnt = 0
idx = 0

while idx < len(p):
    word = ''
    if s.find(p[idx:]) != -1:
        cnt += 1
        break
    for j in range(idx, len(p)):
        word += p[j]
        if s.find(word) == -1:
            cnt += 1
            idx = j
            break

print(cnt)