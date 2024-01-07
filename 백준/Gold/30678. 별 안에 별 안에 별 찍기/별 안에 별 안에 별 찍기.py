import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
tmp = [0, 2, 10, 50, 250, 1250]
# 재귀함수
def star(n):
    if n == 0:
        return '*'
    if n == 1:
        return ['  *  ', '  *  ', '*****', ' *** ', ' * * ']

    stars = star(n - 1)
    result = []

    for i in stars:
        result.append(' ' * tmp[n] + i + ' ' * tmp[n])
    for i in stars:
        result.append(' ' * tmp[n] + i + ' ' * tmp[n])
    for i in stars:
        result.append(i * 5)
    for i in stars:
        result.append(' ' * (5 ** (n-1)) + i * 3 + ' ' * (5 ** (n-1)))
    for i in stars:
        result.append(' ' * (5 ** (n-1)) + i + ' ' * (5 ** (n-1)) + i + ' ' * (5 ** (n-1)))

    return result

# N = 1, 2, 3    / * 0 * 6 5 ** N // 2
# 공백 = 2 10 50 / 0 2 12
# 공백2 = 1 11
# patten = ['  *  ', '  *  ', '*****', ' *** ', ' * * ']

result = star(N)

for i in result:
    print(i)