N, M = map(int, input().split())
if N == 1:
    print(1)
elif N == 2:
    if M < 7:
        print((M + 1) // 2)
    else:
        print(4)
elif N >= 3:
    if M <= 4:
        print(M)
    elif 5 <= M <= 6:
        print(4)
    else:
        print(M - 2)