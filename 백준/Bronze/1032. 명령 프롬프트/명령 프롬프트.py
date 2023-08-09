import sys

T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    # 파일명을 2차원 배열로 입력받는다
    file = [list(sys.stdin.readline().rstrip()) for _ in range(T)]
    result = ''
    for j in range(len(file[0])):
        check = set()
        for i in range(T):
            check.add(file[i][j])

        # 다른문자가 2개 이상 있다면 ? 을 넣는다
        if len(check) > 1:
            result += '?'
        # 한개의 문자로 통일된 경우 해당 문자를 넣는다
        else:
            result += list(check)[0]

    print(result)