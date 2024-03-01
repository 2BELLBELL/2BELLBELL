import sys
input = sys.stdin.readline


def check(number):
    for i in primes:
        for j in primes:
            for k in primes:
                if i + j + k == number:
                    print(i, j, k)
                    return
    print(0)

primes = []
array = [True] * 1001
array[0] = array[1] = True
for i in range(2, 998):
    if array[i]:
        primes.append(i)
    for j in range(2 * i, 997, i):
        array[j] = False

T = int(input())
for _ in range(T):
    K = int(input())
    check(K)