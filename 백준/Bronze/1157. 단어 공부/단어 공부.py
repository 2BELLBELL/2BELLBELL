# 문자를 전부 대문자로 입력 받는다
word = list(input().upper())

# 아스키코드 숫자로 변환한다
word_ord = [ord(i) for i in word]
dic = {}
for j in range(65, 91):
    dic[j] = word_ord.count(j)
key_list = (list(dic.keys()))
value_list = (list(dic.values()))

if value_list.count(max(value_list)) >= 2:
    print('?')
else:
    print(chr(key_list[value_list.index(max(value_list))]))