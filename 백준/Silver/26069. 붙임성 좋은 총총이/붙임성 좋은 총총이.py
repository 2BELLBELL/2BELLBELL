import sys

N = int(sys.stdin.readline())
# 춤추고 있는 사람
dancing = set()

for _ in range(N):
    A, B = sys.stdin.readline().split()
    # 처음으로 총총이가 등장하는 경우
    if A == 'ChongChong' or B == 'ChongChong':
        # 둘 다 dancing set 에 넣는다
        dancing.add(A)
        dancing.add(B)
    # 이후 춤추고 있는 사람을 만나는 경우
    elif A in dancing or B in dancing:
        # 둘 다 dancing set 넣는다
        dancing.add(A)
        dancing.add(B)

print(len(dancing))
