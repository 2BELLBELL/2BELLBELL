import sys
input = sys.stdin.readline


def check(num):
    for i in range(1, len(num) // 2 + 1):
        if num[-i:] == num[-(i * 2):-i]:
            return False
    else:
        return True


def back(num):
    if len(num) == N:
        print(num)
        exit()
    for i in range(1, 4):
        if check(num + str(i)):
            back(num + str(i))
    return



N = int(input())
back('1')