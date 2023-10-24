n = int(input())
a, b = map(int, input().split())
m = int(input())
flow = []
dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    flow.append(int(input()))


def go(x, door1, door2):
    if x == m:
        return 0
    val = flow[x]
    dp[val][door1][door2] = min(
        abs(val - door1) + go(x+1, val, door2), abs(val - door2) + go(x+1, door1, val))
    return dp[val][door1][door2]

print(go(0, a, b))

''' 대실패
def dfs(x, y, cnt):
    global answer, visit
    if visit.count(False) == 0:
        answer = min(cnt, answer)
        return

    for i in range(length):
        if not visit[i]:
            if order[i] <= x and order[i] <= y:
                small = min(x, y)
                large = max(x, y)
                visit[i] = True
                arr[order[i]] = 0
                arr[small] = 1
                dfs(order[i], large, cnt + abs(small - order[i]))
                arr[small] = 0
                visit[i] = False
                arr[order[i]] = 1
            elif order[i] >= x and order[i] >= y:
                small = min(x, y)
                large = max(x, y)
                visit[i] = True
                arr[order[i]] = 0
                arr[large] = 1
                dfs(order[i], small, cnt + abs(large - order[i]))
                arr[large] = 0
                visit[i] = False
                arr[order[i]] = 1
            else:
                visit[i] = True
                arr[order[i]] = 0
                arr[x] = 1
                dfs(order[i], y, cnt + abs(x - order[i]))
                arr[x] = 0
                arr[y] = 1
                dfs(x, order[i], cnt + abs(y - order[i]))
                visit[i] = False
                arr[order[i]] = 1
                arr[y] = 0


# 벽장의 개수
wall_closet = int(input())
n, m = map(int, input().split())
length = int(input())
arr = [1] * wall_closet
order = []
visit = [False] * length
answer = 99999999

for _ in range(length):
    order.append(int(input()) - 1)

arr[n - 1] = 0
arr[m - 1] = 0
# x, y = 열린 문 / cnt =  이동 횟수
dfs(n - 1, m - 1, 0)

print(answer)
'''