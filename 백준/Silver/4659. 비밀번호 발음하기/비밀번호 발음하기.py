mo = ['a', 'e', 'i', 'o', 'u']
while True:
    word = input()
    # 종료 조건
    if word == 'end':
        break

    # 1. 모음이 하나도 포함되지 않은 경우
    flag = False
    for i in mo:
        if i in word:
            flag = True
    if not flag:
        print(f'<{word}> is not acceptable.')
        continue

    # 2. 모음 또는 자음이 3개 연속으로 오는 경우
    result = True
    for i in range(len(word) - 2):
        if word[i] in mo and word[i+1] in mo and word[i+2] in mo:
            result = False
        elif not(word[i] in mo) and not(word[i+1] in mo) and not (word[i+2] in mo):
            result = False
    if not result:
        print(f'<{word}> is not acceptable.')
        continue

    # 3. 같은 글자가 연속으로 두번 오는 경우(ee, oo 제외)
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            else:
                result = False

    if not result:
        print(f'<{word}> is not acceptable.')
        continue

    print(f'<{word}> is acceptable.')