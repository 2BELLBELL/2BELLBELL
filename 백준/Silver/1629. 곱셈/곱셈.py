def dac(a, b, c):
    # b가 1인 경우 a % c 를 반환
    if b == 1:
        return a % c
    # b가 짝수인 경우 2번 형태로 변경 후 재귀
    elif b % 2 == 0:
        return (dac(a, b//2, c)**2) % c
    # b가 홀수면 3번 형태로 변경 후 재귀
    else:
        return ((dac(a, b//2, c)**2)*a) % c

a, b, c = map(int, input().split())
print(dac(a, b, c))