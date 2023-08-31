dp = [0] * 224
for i in range(1, 224):
    dp[i] = i**2

n = int(input())

if n in dp:
    print(1)
else:
    for i in range(1, 224):
        for j in range(1, 224):
            if dp[i] + dp[j] == n:
                print(2)
                exit()
    for i in range(1, 224):
        for j in range(1, 224):
            for k in range(1, 224):
                if dp[i] + dp[j] + dp[k] == n:
                    print(3)
                    exit()
    print(4)

