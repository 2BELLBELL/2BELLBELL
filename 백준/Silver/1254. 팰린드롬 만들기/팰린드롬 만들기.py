word = input()
re_word = word[::-1]
max_v = 0

for i in range(1, len(word) + 1):
    if re_word[:i] == re_word[:i][::-1]:
        max_v = i

print(len(word) * 2 - max_v)