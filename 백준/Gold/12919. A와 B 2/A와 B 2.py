from collections import deque
# bfs 함수 정의
def bfs(string):
    global answer
    # 시작 문자열을 q에 삽입한 채 시작
    q = deque([string])
    while True:
        tmp_string = q.popleft()
        # 현재 문자열과 정답 문자열이 같으면 answer 를 1로 변경
        if tmp_string == word:
            answer = 1
            return
        # 현재 문자열의 길이가 정답 문자열보다 짧아졌다면 중지
        if len(tmp_string) < len(word):
            return
        # 2가지 경우의 수 q에 삽입
        if tmp_string[-1] == 'A':
            q.append(tmp_string[:len(tmp_string) - 1])
        if tmp_string[0] == 'B':
            q.append(tmp_string[1:len(tmp_string)][::-1])
        if not q:
            return

# 입력 값 받기
word = input()
ans_word = input()
answer = 0
# 함수 실행
bfs(ans_word)
print(answer)