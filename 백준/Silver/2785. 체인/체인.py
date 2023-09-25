N = int(input())
chain = list(sorted(map(int, input().split())))
idx = 0
cnt = 1
answer = 0
while idx != N:
    if chain[idx] > 0:
        chain[-cnt] = 0
        chain[-cnt - 1] = 0
        answer += 1
        cnt += 1
        chain[idx] -= 1
    else:
        idx += 1

print(answer)