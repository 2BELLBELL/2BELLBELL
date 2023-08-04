import sys
n = int(sys.stdin.readline())

check = set()

for _ in range(1, n + 1):
    # 이름과 출입 기록을 각각의 변수로 입력받는다
    name, record = sys.stdin.readline().split()
    # 출입 기록이 '출근'이면 set에 이름을 삽입한다
    if record == 'enter':
        check.add(name)
    # 출입 기록이 '퇴근'이면 set에서 해당 이름을 제거한다
    else:
        check.remove(name)

# 정렬 후 역순 만들기
result = sorted(check)
result.reverse()
# 순회하며 출력
for i in result:
    print(i)