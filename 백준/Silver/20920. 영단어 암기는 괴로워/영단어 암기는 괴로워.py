import sys

N, M = map(int, sys.stdin.readline().split())
word_dic = {}

for _ in range(N):
    word = sys.stdin.readline().strip()
    # 외워야하는 단어가 들어온 경우
    if len(word) >= M:
        # 단어장에 안들어가 있으면 0으로 새로 만든다
        if word not in word_dic:
            word_dic[word] = 0
        # 단어장에 이미 들어가 있으면 1을 더해준다
        else:
            word_dic[word] += 1

word_lst = sorted(word_dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in word_lst:
    print(i[0])