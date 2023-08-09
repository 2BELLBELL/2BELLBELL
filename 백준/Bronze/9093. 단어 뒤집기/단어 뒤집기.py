import sys

T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    # 문장을 각각의 단어로 쪼개서 리스트로 입력 받는다
    sen = list(sys.stdin.readline().split())
    result = ''

    for i in sen:
        word = ''
        # 각각의 단어를 선회하며 뒤집기
        for j in i:
            word = j + word
        # 뒤집은 단어를 result 문장에 더한다
        result += word + ' '

    print(result)