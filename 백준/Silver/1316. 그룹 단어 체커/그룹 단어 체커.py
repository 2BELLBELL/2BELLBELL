N = int(input())

# 테스트 케이스만큼 실행
for _ in range(N):
    word = list(input())
    # 2번째 뒤 이상 알파벳과 같으면 그룹 X
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 2:]:
            N -= 1
            break

print(N)

