T = int(input())
for tc in range(T):
    n = int(input())
    answer = 1
    answer += n // 2
    answer += n // 3
    while n > 3:
        n -= 3
        answer += n // 2
    print(answer)