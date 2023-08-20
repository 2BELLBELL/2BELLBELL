# 테스트 케이스의 숫자
N = int(input())

card_list = list(range(1, N + 1))

while len(card_list) > 1:
    if len(card_list) % 2 == 1:
        t = [card_list[-1]]
        t.extend(card_list[1::2])
        card_list = t

    else:
        card_list = card_list[1::2]

print(card_list[0])