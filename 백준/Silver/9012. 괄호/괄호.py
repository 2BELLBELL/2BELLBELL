import sys

# 온점이 나올때까지 입력 받아서 개행문자 제거 후 balance 리스트에 삽입
T = int(input())

# 한줄씩 실행
for i in range(1, T + 1):
    st = sys.stdin.readline().strip()
    # 짝 맞게 붙어있는 괄호가 없을때까지 짝 맞는 괄호 삭제
    while '()' in st:
        if st.find('()') >= 0:
            st = st.replace('()', '')
    # 괄호가 전부 없어졌으면 yes
    if len(st) == 0:
        print('YES')
    # 남은 괄호가 있는 경우 no
    else:
        print('NO')