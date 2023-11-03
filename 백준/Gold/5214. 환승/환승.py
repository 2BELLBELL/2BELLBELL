N, K, M = map(int, input().split())
dp = [-1] * (N + 1)
links = []
stack = set()
num = 3
for _ in range(M):
    link = set(map(int, input().split()))
    if 1 in link:
        for i in link:
            if i != 1 and dp[i] == -1:
                dp[i] = 2
                stack.add(i)
    else:
        links.append(link)
dp[1] = 1



while True:
    tubes = set()
    if dp[N] != -1:
        break
    flag = True
    table = []
    for link in links:
        if len(link.intersection(stack)) == 0:
            table.append(link)
        else:
            for i in list(link - stack):
                tubes.add(i)
                flag = False
    # print(f'links: {links}')
    # print(f'stack: {stack}')
    # print(f'tubes: {tubes}')
    # print()
    if flag:
        print(-1)
        exit()
    for i in list(tubes):
        if dp[i] == -1:
            dp[i] = num
    num += 1
    stack.clear()
    stack = tubes
    links = table

# print(f'dp: {dp}')
print(dp[N])
